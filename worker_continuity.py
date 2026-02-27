#import pandas for data transformation and storage
import pandas as pd

#Assuming the is in the directory where the program is run 
try:
    
    dataset = pd.read_csv("worker_activity.csv")
    
#Otherwise provide the right directory to the dataset    
except FileNotFoundError:
    try:
        
        data_directory = input("Enter dataset directory->>")
        dataset = pd.read_csv(data_directory)
        
    except FileNotFoundError:
    
        print("The file directory is not correct. So this algorithm will not run. \nRemember to append .csv to the end of the directory and do no enclose with a quotation mark.")
def work_continuity(dataset):
    
    """
    This function obtain the continuity of work for each user.
    
    Input: Pandas DataFrame object
    Output: Pandas DataFrame object with Worker and continuity as columns
    """
    
    #import datetime module for datetime parsing
    from datetime import datetime

    
    # check if the input is a DataFrame
    if isinstance(dataset,pd.DataFrame):
        try:
            #For consistency, we will sort the dataset by Worker and assign it to a new Object
            new_data = dataset.sort_values(by=["Worker"]).reset_index(drop=True)
            
        except KeyError:
        
            return "Your dataset does not have Worker column. So this algorithm will not run"
        finally:
            #Let's declare a counter container as a an empty dictionary 
            continuity = {}
            
            #Then, we loop through the dataset rows and check for the conditions
            for x in range(1,len(new_data)):
                
                y = new_data.loc[x-1, "Worker"]
                
                continuity.setdefault(y, 1)
                
                # Set date format string
                str_date_format = "%d/%m/%Y %H:%M"
                
                # Check if a worker is active
                is_active = abs((datetime.strptime(new_data['Date'][x], str_date_format)-
                                 datetime.strptime(new_data['Date'][x-1], str_date_format)).days)<=6

                # Check if a worker did not switch to a different employer
                isnot_change_employer = new_data.loc[x, 'Employer'] == new_data.loc[(x-1), 'Employer']
                
                # Check if a worker did not switch to a different role
                isnot_change_role = new_data.loc[x, 'Role'] == new_data.loc[(x-1), 'Role']
                
                # Check if a worker is active and did not switch employer and role
                if isnot_change_employer and isnot_change_role and is_active:
                    continuity[y] += 1
                else:
                    continuity[new_data.loc[x, 'Worker']] = 1
                    
            #save the result into a DataFrame object
            final_data = pd.DataFrame(zip(continuity.keys(),continuity.values()),columns=["Worker","Continuity"])
            
            #sort the Dataframe with respect to Continuity (In descending order)
            final_data.sort_values(by="Continuity",ascending = False,inplace=True)

            #save the data as "results.csv"
            return final_data.to_csv("results.csv",index=False)
    else:
        return f"The algorithm expect a DataFrame object, however a {type(dataset)} object was passed"
            
# run if imported directly
if __name__ =="__main__":
    work_continuity(dataset)
