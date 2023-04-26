let data = [
  {
    name: "John",
    age: 25
  },
  {
    name: "Mary",
    age: 30
  },
  {
    name: "Steve",
    age: 28
  },
];

let xx = data.filter(function (x) {
  return x.age >= 28;
}).map(function (x) {
    return x.name;
});


console.log(xx);