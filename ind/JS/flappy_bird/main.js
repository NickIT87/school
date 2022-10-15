const main = (n) => {
    console.log(n)
}

const main2 = function() {
    console.log(n)
}

function main3() {
    console.log(n)
    let b = 4
}

const obj = {
    "greet": "hello"
}

console.log(obj['greet'])

class Student {
    greeting = "hello"

    constructor(name, email) {
        this.name = name
        this.email = email
    }
}

const stud = new Student('Василь Петрович Іванов', 'vt@gmail.com')

console.log(stud.name, stud.greeting)