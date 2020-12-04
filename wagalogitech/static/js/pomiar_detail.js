console.log("organizacja_detail.js")

let start_owner=''
let start_czyWazny=''
let start_wartosc=''
let start_data_pomiaru=''

$(document).ready(function() {
   console.log("pomiar szczegoly")
   let searchParams = $(location).attr('href')
   let destinationURL = searchParams.replace("front", "api/v1")
   console.log("current url: " +destinationURL)
   $.ajax({
      url: destinationURL,
      type: "GET",
   }).done(function(response) {
      console.log("udalo sie pobrac z ajaksa dane !")
      $('#owner').attr('value', response.owner)
      $('#czyWazny').attr('value', response.czyWazny)
      $('#wartosc').attr('value', response.wartosc)
      $('#data_pomiaru').attr('value', response.data_pomiaru)
   }).fail(function() {
      alert("Wystąpił błąd w połączeniu z djangorestapi")
   }).then(function() {
      start_owner=$("#owner").val()
      start_czyWazny=$("#czyWazny").val()
      start_wartosc=$("#wartosc").val()
      start_data_pomiaru=$("#data_pomiaru").val()
   })
})