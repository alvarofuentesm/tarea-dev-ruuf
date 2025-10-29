from typing import List, Dict
import json
import itertools

# intentar agregar el panel. origin_x y origin_y correspondenden a las coordenadas de la esquina superior izquierda del panel
def add_to_positions(origin_x: int, origin_y: int, panel_width: int, panel_height: int, 
                     positions: list, panel_index: int, rotate: bool = False):
    
    if (rotate): # girar panel
        panel_width_temp = panel_width
        panel_width = panel_height
        panel_height = panel_width_temp

    if ( (origin_x + panel_width  ) > len(positions) ): # fuera de limite
        return False
    
    if ( (origin_y + panel_height  ) > len(positions[0]) ): # fuera de limite
        return False
    
    temp_positions = []
    for pos in positions:
        temp_positions.append(pos.copy())
    
    for y in range(panel_height):
        for x in range(panel_width):
            #print("trying to put in : ", (x + origin_x, y + origin_y))
            if(temp_positions[x  + origin_x][y + origin_y] == 0):
                temp_positions[x + origin_x][y + origin_y] = panel_index
            else:
                return False
                
    for i, pos in enumerate(temp_positions):
        for j, value in enumerate(pos): 
            positions[i][j] = value

    return True

# agregar paneles al techo segun la permutacion de posiciones
def add_to_roof_permutation(panel_width: int, panel_height: int, 
                roof_width: int, roof_height: int, positions: list, permutation: list,
                total_panels: int, space_left: int):
    
    panel_index = 0
    for x in range(roof_height): 
        for y in range(roof_width):
            success = add_to_positions(x, y, panel_width, panel_height, positions, panel_index + 1, permutation[panel_index])

            if (success):
                panel_index += 1
                total_panels += 1
                space_left -= panel_height*panel_width
            
                if (space_left == 0 or panel_index == len(permutation)):
                    return total_panels, space_left

    return total_panels, space_left

# llenar con valores cero las posiciones
def empty_positions(positions: list, roof_height: int, roof_width: int):
    # representar las posiciones en el roof
    # ejemplo "roofW": 2, "roofH": 4
    # =>
    # [ 
    # [0, 0],
    # [0, 0],
    # [0, 0],
    # [0, 0]
    # ]
        
    for y in range(roof_height): # todos vacios al inicio
        positions.append([])
        for x in range(roof_width):
            positions[y].append(0)

# mostrar solucion
def show_solution(positions: list):
    print("Solution: ")
    for pos in  positions:
        print(pos)

def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    # Implementa acá tu solución
 
    # calcular el maximo de paneles para reducir busqueda
    # por ejemplo: 
    # 
    #  "panelW": 1, "panelH": 2, "roofW": 2, "roofH": 4,
    # => (2*4) // (1*2) = 8//2 = 4 paneles como maximo
    #
    #  "panelW": 1, "panelH": 2, "roofW": 3, "roofH": 5,
    # => (5*3) // (1*2) = 15//2 = 7
    
    max_panels = (roof_width * roof_height)//(panel_width * panel_height)

    # determinar las posibles orientaciones de los paneles 
    # por ejemplo para 2 paneles con dos combinaciones: 
    # [horizontal, horizontal]
    # [horizontal, vertical]
    # [vertical, horizontal]
    # [vertical, vertical]
    # => son 2**2 = 4 combinaciones
    
    # se representa horizontal con False y vertical con True
    permutations = list(itertools.product([False, True], repeat=max_panels))  

    best_solution = []
    empty_positions(best_solution, roof_height, roof_width)
    best_space_left = roof_width * roof_height 
    best_total_panels = 0


    for permutation in  permutations[:len(permutations)//2]: # por simetria del escenario puedo revisar solamente la mitad 

        space_left = roof_width * roof_height # funcion de costo
        total_panels = 0
        positions = []
        
        empty_positions(positions, roof_height, roof_width)
        
        total_panels, space_left = add_to_roof_permutation(panel_width, panel_height, roof_width, roof_height, 
                                                           positions, permutation, total_panels, space_left)
        
        if (space_left < best_space_left): # almacenar mejor solucion
            best_space_left = space_left
            best_total_panels = total_panels

            for i, pos in enumerate(positions):
                for j, value in enumerate(pos): 
                    best_solution[i][j] = value

        if (space_left == 0 or total_panels == max_panels): # mejor solucion alcanzada 
            show_solution(positions)

            return total_panels
        
    show_solution(best_solution)
    return best_total_panels


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
    #with open('test_cases_extended.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()