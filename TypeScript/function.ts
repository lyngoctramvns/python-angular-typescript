function addTwo(num) {
    return num + 2
}

addTwo(5)

//The num parameter here has any => not good

function fixAddTwo(num: number){
    return num + 2
}

fixAddTwo(5)

//Remember to indicate the type for parameters in function for TypeScript

export{}