# 2877. Create a DataFrame from List
import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    one, two=[i[0] for i in student_data], [i[1] for i in student_data]
    df= pd.DataFrame({"student_id":one, "age": two})
    return df

# 2878. Get the Size of a DataFrame
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
# 2879. Display the First Three Rows
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
# 2880. Select Data  "RE"
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101][["name", "age"]]