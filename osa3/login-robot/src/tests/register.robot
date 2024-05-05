*** Settings ***
Library    ../AppLibrary.py

Resource    resource.robot
Test Setup    Input New Command And Create user
*** Test Cases ***
#Register With Valid Username And Password
# ...
#    Create User    kallek    kelakala10!
#    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Create User    velmuk    kolakala9
    Create User    velmuk    jabadaba210
    Output Should Contain    User with username velmuk already exists

Register With Too Short Username And Valid Password
# ...
    Create User    je    kelakela11
    Output Should Contain    Username is too short

Register With Enough Long But Invalid Username And Valid Password
# ...
    Create User    jea18!!    kalakala17
    Output Should Contain    Invalid characters in username

Register With Valid Username And Too Short Password
# ...
    Create User    jeajea    j4a
    Output Should Contain    Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
# ...
    Create User    userjea    eimerkkeja
    Output Should Contain    Password not strong enough

*** Keywords ***

Input New Command And Create user
    Input New Command
    Create User    velmuk    kokolala19
    Input New Command
