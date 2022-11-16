// var url = 'https://api.adviceslip.com/advice'
// var request = new XMLHttpRequest();

// fetch(url, {
//   method: 'GET'
// }).then((response) => {
//   response.json().then((jsonResponse) => {
//     console.log(jsonResponse)
//   })
//   // assuming your json object is wrapped in an array
//   response.json().then(i => i.forEach(i => console.log(i.advice)))
// }).catch((err) => {
//   console.log(`Error: ${err}` )
// });
    



var json = '{"nome": "Jesiel", "idade": "22"}'

var obj = JSON.parse(json)

console.log(obj.nome)

function copy() {
  var text = document.getElementsByClassName("card-text");
navigator.clipboard.writeText(text).then(function() {
  console.log(text.value);
}, function(err) {
  console.error('Async: Could not copy text: ', err);
});
}