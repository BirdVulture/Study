
//https://www.youtube.com/watch?v=CGdcHl8ExcM&list=PLUb9K99oQb2u1swlk6TTuV1vnMEG8ktfV&index=1&pp=iAQB


// КОНСТАНТЫ И ПЕРЕМЕННЫЕ

let greetings = "Hello" // Константа

var direction = "Left" // Переменная

direction = "Right" // Переназначение переменной

// ТИПЫ ДАННЫХ

var number: Int = 1

var numDouble: Double = 1.5
var numFloat: Float = 1.5
var greeting1: String = "Hello "
var greeting2: String = "World"

var greetingsum = greeting1 + greeting2 // Конкатенация строк

var greeting3 = "Hello, \(greeting2)" // Интерполяция строк

print(greeting3)

var areYouHappy: Bool = true

//БАЗОВЫЕ ОПЕРАТОРЫ

//Унарные: префиксные -a, !b постфиксные с!
//Бинарные: инфиксные a + b
//Тернарные: a ? b : c

//Оператор присваивания
var a = 12

var b = 5

//b = a

// Арифметические операторы +, -, *, /, % (остаток от деления)

var c = a + b
c = a - b
c = a * b
c = a / b

c = a % b

//Составные операторы присваивания +=, -=

c += 2 // c = c + 2

// Счетчик

var counter = 0

counter += 1

// Операторы сравнения ==, !=, >, <, <=, >=

c > a

//Тернарный условный оператор
//выражение ? действие 1 : (иначе) действие 2

//с помощью if
if a == b {
    print("a = b")
} else {
    print("a != b ")
}
// с помощью тернарного оператора
a == b ? print("a = b") : print("a != b ")

// Оператор замкнутого/закрытого (a...b) диапазона и полузамкнутого/полузакрытого диапазона (a..<b)


// Логические операторы !a (не равно) && (И) || (ИЛИ)

let isTheWeatherGood = true

areYouHappy = true

if areYouHappy && isTheWeatherGood {
    print("Go outside")
} else {
    print("Stay home")
}

// УСЛОВИЯ

let firstCard = 10
let secondCard = 10

if firstCard + secondCard == 21 {
    print("You are win")
} else if (firstCard + secondCard) > 18 && (firstCard + secondCard) < 21 {
    print("Good cards")
} else {
    print("Regular cards")
}

let age1 = 18
let age2 = 21

if age1 > 18 && age2 > 18 {
    print("Both are other 18" )
}

let weather = "sunny"

switch weather {
case "rain": print("Bring an umbrella")
case "snow": print("Wrap it warm")
case "sunny": print("Wear glasses")
    fallthrough //Провалиться дальше
default: print("enjoy")
}

switch age1 {
case 0...10: print("You are too young")
case 13..<20: print("You are teenager")
case 20...60: print("You are grown man")
case 80...: print("You are old man")
default: print("How old are you?")
}

//ЦИКЛЫ for in / while / repeat while

let count = 1...3

for number in count {
    print("Number is \(number)")
    
}

for index in 0...3 {
    print("\(index) умножить на 3 равно \(index * 3)")
}

var number1 = 1

while number1 <= 3 {
    print(number1)
    number1 += 1
}

print("Start!")

//СОСТАВНОЙ ТИП ДАННЫХ tuple используется для временного хранения данных

var person = (name: "Igor", age: 40, isMarried: true, weight: 70.5)

var tuple1 = (a, b)

var tuple2 = (10, "Hello")

var tuple3: (Int, String)

var tuple4 = (name: "Igor", age: 40, isMarried: true, weight: 70.5)

tuple4.0
tuple4.1

tuple4.name
tuple4.age

var (name, age, isMarried, weight) = tuple4 //разборка tuple4 на элементы

name
age
isMarried
tuple4


// ОПЦИОНАЛЬНЫЕ ТИПЫ ДАННЫХ

var age11: Int? = 12

age11 = nil

// 1 force unwrapping ---!
if age11 == nil {
    print("age is nil")
} else {
    age11! + 1
    
}


//2 Optional binding
let str1  = "5"

let num1 = Int(str1)

if var safeAge = age11 {
    safeAge += 1
}

let yearOfBirth = "1980"

if let safeYearOfBirth = Int(yearOfBirth) {
    safeYearOfBirth
}

// 3 Опциональное связование ??

var example: String? = "Hello"

print(example ?? "example = nil")

// 4 Неявно извлеченные опционалы

// int, Int?, Int!

var num2: Int! = nil

num2 = 10

num2 = num2 + 1



// КОЛЛЕКЦИИ: массивы, множества, словари
// Array Массив

var arr1 = Array<String>()

var arr2 = [String]()

let apple = "apple"
let lemon = "lemon"
let orange = "orange"
let strawberry = "strawberry"

let fruits = [apple, lemon, orange, strawberry]

var shoppingList = ["eggs", "milk", "bread", "flour", "sweets"]

// Доступ к массиву - через методы или через индексы
// методы
shoppingList.count // счет количества элементов в массиве

shoppingList.isEmpty // проверка на наличие значений

shoppingList.append("butter") // добавление в конец списка

shoppingList.insert("sugar", at: 0) // вставка нового элемента на место старого по индексу

// доступ через индексы
shoppingList[0]

shoppingList[1] = "salt" // переназначение элемента массива

// Перебор элементов массива через цикл

for i in shoppingList {
    print(i)
}

//индексы и значения массива через цикл

for (index, value) in shoppingList.enumerated() {
    print("Index \(index): \(value) ")
}

// сложение массивов

shoppingList += ["pepper"]

var numb1 = [1, 2, 3, 4, 5]
var numb2 = [6, 7, 8, 9]

var numb3 = numb1 + numb2

// SET Множество - когда порядок не важен, все значения - уникальные

var set = Set<String>()

var listOfSports: Set = ["Babminton", "Bowling", "Tennis", "Hockey"]

// методы для работы множеством

listOfSports.count //подсчет количества элементов в множестве

listOfSports.isEmpty // проверка на наличие значений

listOfSports.insert("Fishing") //вставка нового элемента

listOfSports.remove("Bowling")

listOfSports

listOfSports.contains("Tennis") //проверка наличия значения в множестве

// работа с сетом через итерации (в цикле)

for i in listOfSports {
    print(i)
}

listOfSports.sorted() // сортировка множества

for i in listOfSports.sorted() {
    print(i)
}

// Преобразование массива в множество

let colors1 = ["red", "green", "blue", "red", "green", "blue"]

let colors2 = Set(colors1)

// базовые операции с множествами

let oddNumbers: Set = [1, 3, 5, 7, 9] // нечетные числа

let evenNumbers: Set = [0, 2 ,4, 6, 8] // четные числа

let primeNumbers: Set = [2, 3, 5, 7] // простые числа

// объединенние двух множеств в третье
oddNumbers.union(evenNumbers).sorted()

// создание множества из общих значений двух других множеств

oddNumbers.intersection(evenNumbers).sorted()
oddNumbers.intersection(primeNumbers).sorted()

//вычитание одного множества из другого

oddNumbers.subtracting(primeNumbers).sorted()

// создание множества из неповторяющихся значений двух других множеств

oddNumbers.symmetricDifference(primeNumbers).sorted()

//Dictionary - словарь Ключ - значение [key: value]

var diction = [Int: String]()

var heights = ["Ian": 1.75, "Maria": 1.76, "Igor": 1.82, "Olga": 1.56]

// работа со словарем по ключу

heights["Ian"]

var results1 = ["Mathematics": 100, "English": 85, "Geography": 75]

results1["English"]

results1.count //подсчет количества элементов
results1.isEmpty //проверка на наличие значений
results1["History"] = 80 // добавление элемента в словарь
results1["History"] = 90

results1["History"]

//обновление значений через методы

results1.updateValue(70, forKey: "History")
results1["History"]

//удаление пары ключ-значение из словаря

results1.removeValue(forKey: "History")
results1["History"]

// итерации со словарем через цикл

for (subject, point) in results1 {
    print("\(subject): \(point) ")
}

for subject in results1.keys {
    print("Subject: \(subject)")
}

for point in results1.values {
    print("point: \(point)")
}

// преобразование в массивы

var keys = Array(results1.keys)
var values = Array(results1.values)

// ФУНКЦИИ

// Объявление и вызов функций

func greetFunc() {
    print("Hello")
}

greetFunc()

// Принимать

func square(number: Int) {
    print(number * number)
}

square(number: 3)


// Возвращать значение в переменную

func square1 (number: Int) -> Int {
    return number * number
}

var result123 = square1(number: 5)

print(result123)

// Возвращать несколько значений в tuple

// Решение 1
func getUser() -> [String] {
    return ["Ivan", "Ivanov"]
}

let user1234 = getUser()

print(user1234[0])


// решение 2
func getUser1() -> [String: String] { // функция возвращает словарь
    return ["firstName": "Ivan", "secondName": "Ivanov"]
}

let user22 = getUser1()

print(user22["secondName"] ?? "not found")

// решение 3 - с помощью tuple

func getUser2() -> (first: String, second: String) {
    return (first: "Ivan", second: "Ivanov")
}

let user23 = getUser2()

print(user23.first)


// Имена параметров

func sayHello(to name: String) {
    print("Hello \(name)")
}

sayHello(to: "Ian")

// Пропуск имен параметров

func sayHello2(_ person: String) {
    print("Hello \(person)")
}

sayHello2("Ian")

// Параметры по умолчанию

func greet3(_ person: String, nicely: Bool = true) {
    
    if nicely == true {
        print("Hello, \(person)")
    } else {
        print("oh no, it's \(person) again")
    }
}

greet3("Maria") // по умолчанию nicely = true


// Вариативные функции и вариативные параметры - принимает любое количество параметров одного типа

func squareVar(numbers: Int...) {
    for num in numbers {
        print("number \(num)")
    }
}

squareVar(numbers: 1, 2, 3, 4)

// Сквозные параметры

func doubleIt(number: inout Int) {
    number *= 2
}

var myNum = 10

doubleIt(number: &myNum)


// КЛОУЖЕРЫ - анонимные функции

let driving = {
    print("I'm driving in my car") // Клоужер ничего не принимает, только печатает
}

// вызов клоужера

driving()

let driving2 = { (place: String) in // Клоужер принимает параметр и печатает
    print("I'm going to \(place)")
    
}

driving2("home")

// функция и клоужер

func pay2(user: String, amount: Int) {
    //
}

let payment2 = { (user: String, amount: Int) in // in показывает, где начинается тело клоужера
        //code
}

let driving3 = { (place: String) in // Клоужер принимает параметр и печатает
    return "I'm going to \(place)"
    
}

let message1 = driving3("London")

print(message1)

// клоужер возвращает значение

let payment3 = { (user: String, amount: Int) -> Bool in
    print("paying \(user)")
    return true
}

//13.30

// передача клоужера в функцию на примере клоужера driving

func travel(action: () -> Void) {
    print("I'm getting ready to go")
    action()
    print("I arrived")
}


travel(action: driving)

//trailng clouser

travel() {
    print("I'm driving in my car")
}


func animate(duration: Double, animations: () -> Void ) {
    print("Starting a \(duration) second animation")
    animations()
}
            
animate(duration: 3, animations: {
    print("Image")
})

animate(duration: 3) {
    print("Image")
}


func travel2(action: (String) -> Void) {
    print("I'm getting ready to go")
    action("London")
    print("I arrived")
}

travel2(action: { (place: String) in
    print("i'm going to \(place)")
})

let chageSpeed = {(speed: Int) in
    print("Changing speed to \(speed)")
}

func buldCar(name: String, engine: (Int) -> Void) {
    //code
}

func travel3(action: (String) -> String) {
    print("I'm getting ready to go")
    let deskription = action("London")
    print(deskription)
    print("I arrived")
}


travel3(action: { (place: String) -> String in
        return "I'm going to \(place)"
})

//сокращенные имена параметров

travel3(action: { place in
        "I'm going to \(place)"
})

travel3(action: {
        "I'm going to \($0)"
})

func travel4(action: (String, Int) -> String) {
    print("I'm getting ready to go")
    let deskription = action("London", 60)
    print(deskription)
    print("I arrived")
}

travel4(action: {
        "I'm going to \($0) at \($1)"
})

// возврат клоужера из функции

func travel5() -> (String) -> Void {
    return { (place: String) in
        print("I'm going to \(place) ")
    }
}

let resultF5 = travel5()

resultF5("london")

// Захват значений клоужером извне  и работа внутри себя (counter)

func travel6() -> (String) -> Void {
    var counter = 0
    return { (place: String) in
        print("I'm going to \(place) ")
        counter += 1
    }
}

let resultF6 = travel6()

resultF6("london")
resultF6("london")
resultF6("london")

//Перечисления

enum Result {
    case success
    case failure
}
var result4 = Result.failure

result4 = Result.success

result4 = .failure

let result5 : Result

result5 = .success

enum Activity {
    case dancing
    case running
    case talking
    case singing
}

let currentActivity = Activity.dancing

switch currentActivity {
case .dancing: print("Dance")
case .running: print("Run")
case .singing: print("Sogn")
case .talking: print("Talk")
}

enum Activity2 {
    case dancing
    case running(dectination: String)
    case talking(topic: String)
    case singing(volume: Int)
}

let talking1 = Activity2.talking(topic: "Football")

enum Planet: Int {
    case mercury
    case venus
    case earth
    case mars
}


let earth = Planet(rawValue: 3)


enum Phone: String {
    case Apple = "iPhone 8"
    case Samsung = "Galaxy S10"
    case Google = "Pixel 2"

}


let myPhone = Phone.Apple

print(myPhone)
print(myPhone.rawValue)

// КЛАССЫ

class Human {
    //хранимые свойства
    var age: Int // свойство класса
    var name: String
    
    // вычисляемые свойства
    var status: String {
        get {
            if isQualified {
                return "\(name) is qualifies for this job"
            } else {
                return "\(name) is not qualifies for this job"
            }
        }
    }

    /*
    структурная схема вычисляемых свойств
    var имя_свойства: тип_данных {
     get {
        // вычисление значения
     }
     set (параметр) {
        // установка значения
     }
     
     }
    
    
     
     
     
    */
    var isQualified: Bool
    
    func move() {
        print("\(name) is moving") // метод класса
    }
    
    //инициализатор - функция, выполняющая первоначальную инициализацию объекта
    
    init(age: Int, name: String, isQualified: Bool) {
        self.age = age
        self.name = name
        self.isQualified = isQualified
    }
}

// экземпляр класса

var maria = Human(age: 25, name: "Maria", isQualified: true)

maria.age
maria.isQualified
maria.status


class Account {
    //хранимые свойства
    var sum: Double = 0 // Сумма вклада
    var rate: Double = 0.01 // процентная ставка
    
    // вычисляемые свойства
    var profit: Double {
        get{   // возвращает в profit результат операции
            return sum + sum * rate
        }
        
        set(newProfit){ // вводим ожидаемую прибыль и получаем необходимую сумму вклада параметр newProfit на входе - можем называть как угодно
            self.sum = newProfit / (1 + rate)
            
        }
    }
    
    init(sum: Double, rate: Double) {
        self.sum = sum
        self.rate = rate
    }
    
    
}

var myAcc: Account = Account (sum: 1000, rate: 0.1) //создали экземпляр класса Аккаунт

myAcc.profit // использовали get

myAcc.profit = 45000 // установили ожидаемую прибыль

myAcc.sum // необходимая сумма вклада для получения этой прибыли

// Наблюдатели свойств (нету)




//СТРУКТУРЫ

class Human2 {
    var age: Int
    var name: String
    
    init(age: Int, name: String) {
        self.age = age
        self.name = name
    }
}

var human2 = Human2(age: 20, name: "Igor")
// свойства экземпляра класса можно изменять если свойство переменная а класс - константа!!!

human2.age




struct Human3 {
    var age: Int
    var name: String
}

// Для структуры не нужен инициализатор
var human3 = Human3(age: 25, name: "Maria")

// свойства экземпляра структуры можно изменять если свойство и структура - переменные

human3.age
human3.age = 35
human3.age


//value type - Int, String, Bool, struct, Array и др
// при копировании типа значение происходит копирование самого значения, исходный экземпляр не меняется и не связан


// reference type - enum, class

var human31 = Human3(age: 30, name: "Olga")

human31 = human3


var human21 = Human2(age: 50, name: "Stas")

human21 = human2 //скопировали референс в другой экземпляр
human21.age
human21.name

human21.age = 60
human21.name = "Vitaliy"


human2.age // Изменились значения екземпляра, который был приравнен!
human2.name

// Отличия в методах между классом и структурой

class Person2 {
    var name: String
    
    func makeAnonymous() {
        name = "Anonymous"
    }
    
    init(name: String) {
        self.name = name
    }
}

struct Person1 {
    var name: String
    
    mutating func makeAnonymous() { // для метода, изменяющего свойство в структуре, надо добавлять mutating
        name = "Anonymous"
    }
}

// СВОЙСТВА ТИПОВ

class Dog {
    var name: String // Свойство экземпляра
    var age: Int {
        didSet {
            if age > Dog.maxAge {
                age = oldValue
            }
        }
    }
    
    static let maxAge = 30 // static - свойство класса, не экземпляра
    
    nonisolated(unsafe) static var howManyDogs = 0 // количество созданных экземпляров
    
    lazy var questions = "Can I ask a question?" // Инициализируется только тогда, когда к этому свойству обращаются
    
    init(name: String, age: Int) {
        self.name = name
        self.age = age
        Dog.howManyDogs += 1 // счетчик количества экземпляров
    }
}


struct Cat {
    var name: String // Свойство экземпляра
    var age: Int {
        didSet { // наблюдатель свойства если значение было изменено и оно не смоотвествует улсовию - возвращается старое значение
            if age > Cat.maxAge {
                age = oldValue
            }
        }
    }
    
    static let maxAge = 30 // static - свойство структуры, не экземпляра

}

var dog = Dog(name: "Sobaka", age: 5)

var cat = Cat(name: "Koshka", age: 3)

dog.age
dog.age = 35
dog.age

Dog.howManyDogs

var dog1 = Dog(name: "Sobaka1", age: 6)
var dog2 = Dog(name: "Sobaka2", age: 6)


// НАСЛЕДОВАНИЕ
// родительский /супер/ класс и дочерний класс

class Dog2 {
    var name: String
    var breed: String //хранимое свойство
    
    var info: String {
        return "The breed of \(name) is a \(breed)" //getter
    }
    
    func makeNoize() -> String {
        return "Hello"
    }
    
    init(name: String, breed: String) {
        self.name = name
        self.breed = breed
    }
}

class Corgi: Dog2 {
    
    var isHappy: Bool
    
    override var info: String {
        return name + " " + breed
    }
    
    override func makeNoize() -> String {
        return "Hello, Sir" // переопределение функции
    }
    
    init(isHappy: Bool) {
        self.isHappy = isHappy
        super.init(name: "Alisa", breed: "Corgi") // инициализатор свойств родителя
        
    }
    
}

var corgi = Corgi(isHappy: true)

corgi.name = "Alisa"
corgi.makeNoize()

corgi.info

// РАСШИРЕНИЯ

extension Int {
    func squared() -> Int {
        return self * self
    }
    
    
    func repetition(task: () -> Void) {
        for _ in 0..<self {
            task()
        }
    }
    
    var isEven: Bool {
        return self % 2 == 0
    }
    
    
}

var number111 = 3

number111.isEven

number111.repetition {
    print("Hello")
}


number111.squared()

extension Double {
    
    var m: Double {
        return self
    }
    
    var cm: Double {
        return self / 100
    }
    
    var mm: Double {
        return self / 1000
    }
}

var double = 5.0

double.m

double.cm

double.mm

// ПРОТОКОЛЫ - перечень свойств и метододов, которые обязаны  включать в себе те классы и структуры, которые поддерживают этот протокол


protocol ICanBuyIt {
    var label: String { get set }
    var price: Int { get set }
}






struct Milk: ICanBuyIt {
    var label: String
    
    var price: Int
    
}

class Book: ICanBuyIt {
    var label: String
    var price: Int
    
    var amount: Int
    
    init(label: String, amount: Int, price: Int) {
        self.label = label
        self.amount = amount
        self.price = price
    }
}

struct Bread: ICanBuyIt {
    var label: String
    var price: Int
    var color: [String]
}

func buy(_ item: ICanBuyIt) {
    print("I'm buying \(item.label) It cost me \(item.price)")
}

protocol Identifiable {
    var id: String { get set}
}

struct User123: Identifiable {
    var id: String
}

var numb = 24
if numb > 0 {
    print("Ok")
}

