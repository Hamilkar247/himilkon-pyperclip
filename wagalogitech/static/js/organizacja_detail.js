console.log("organizacja_detail.js")

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


// zmienne przechowują dane przeslane z get
let start_nazwa_org=''
let start_opis_org=''

let currentUrl = $(location).attr('href')//w vanilii JS to jestwindow.location.href
let urlsearchParams = currentUrl.split('/')
console.log("tablica elementów: urlsearchParams")
let numberOfOrganization = urlsearchParams[urlsearchParams.length-1]
console.log("Numer elementu:"+ numberOfOrganization)

//wartosci z bazy danych pewnej organizacji
$(document).ready(function() {

   console.log("jestesmy w szczegolach organizacji")
   let destinationURL = currentUrl.replace("front", "api/v1")
   console.log("current url:" + destinationURL)
   $.ajax({
      url: destinationURL, //do poprawienia !!!
      type: "GET",
   }).done(function(response) {
       console.log("udalo sie pobrac z ajaksa dane !")
       $('#nazwa_organizacji').attr('value', response.nazwa);
       $("#opis_organizacji").attr('value', response.opis);
   }).fail(function() {
     alert("Wystąpił błąd w połączeniu z djangorestapi!");
   }).then(function() {
     start_nazwa_org=$("#nazwa_organizacji").val()
     console.log("start_nazwa_org:" + start_nazwa_org)
     start_opis_org=$("#opis_organizacji").val()
     console.log("start_opis_org:" + start_opis_org)
   })
})

function deleteOrganization() {
  //e.preventDefault()
  console.log("funkcja DELETE Ajax")
  console.log("currentURL:" + currentUrl)
  console.log("Numer elementu:"+ numberOfOrganization)
  $.ajax({
    url:  currentUrl,
    type: "DELETE",
    beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    },
  }).done(function(response) {
    console.log("udalo sie usunąć element")
    alert("Usunąłeś element organizacji!")
    //window.location.replace("http://127.0.0.1:8000/front/organizacje/")
  }).fail(function() {
    alert("Wystąpił błąd w połączeniu z djangorestapi!")
  }).then(function() {

  })
}
