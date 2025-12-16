*** Settings ***
Library                Collections
Library                RequestsLibrary
Library                JSONLibrary
Library                OperatingSystem
Resource               ../resources/common.robot
Resource               ../resources/keyword.robot



*** Keywords ***


Data

    ${Json_obj}=       Evaluate                    open('${CURDIR}/../Data/Data.json').read()    json
    ${dataA}=          Evaluate                    json.loads('''${Json_obj}''')       json

    # Extracting data for relationship object and logging the values
    ${data1}=          Set Variable                ${dataA["data1Relationship"]}
    Log                ${data1}
    ${data2}=          Set Variable                ${dataA["data2Relationship"]}
    Log                ${data2}
    ${data3}=          Set Variable                ${dataA["data3Relationship"]}
    Log                ${data3}

    # Setting variables for relationship data
    ${Name}=           Set Variable                ${data1["Relationship Name"]}
    ${Type}=           Set Variable                ${data1["Type"]}
    ${Role}=           Set Variable                ${data1["Role"]}
    ${Name1}=          Set Variable                ${data2["Relationship Name"]}
    ${Type1}=          Set Variable                ${data2["Type"]}
    ${Role1}=          Set Variable                ${data2["Role"]}
    ${Name2}=          Set Variable                ${data3["Relationship Name"]}
    ${Type2}=          Set Variable                ${data3["Type"]}




Adding Relationships

 