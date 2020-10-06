{

  var input1 = prompt("Give a binary number");
  console.log(Number.parseInt(input1,2));

  var a = new Number("101");
  console.log(a);
  console.log(Number.parseInt(input1,2));



  var input2 = Number(prompt("Give a number"));
  // Zo kan je van een string een number maken (dit is gewoon een andere manier)
  console.log(input2, "Decimal to binary", input2.toString(2));
  console.log(input2, "Decimal to octal", input2.toString(8));
  console.log(input2, "Decimal to hexadecimal", input2.toString(16));

  var nb = Number("15");
  console.log(nb + 4);
}
