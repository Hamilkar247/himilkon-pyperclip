console.log("pomiar_detail.js")
let number_of_pomiar=null
let destinationURL=null
let regex = null
function func_for_number_of_pomiar(){
  let url = window.location.href
  table_of_url = url.split('/')
  console.log("table of url" + table_of_url)
  if (table_of_url[table_of_url.length - 1] == '') {
    number_of_pomiar = table_of_url[table_of_url.length - 2]
  }
  else {
    number_of_pomiar = table_of_url[table_of_url - 1]
  }
  console.log("url:"+window.location.href)
  console.log("number_of_pomiar:"+number_of_pomiar)
}

let start_owner=''
let start_czyWazny=''
let start_wartosc=''
let start_data_pomiaru=''

$(document).ready(function() {
   func_for_number_of_pomiar()
   console.log("pomiar_szczegoly.js")
   let searchParams = $(location).attr('href')
   destinationURL = get_urls().url_home + get_urls().api_v1_pomiar +number_of_pomiar
   console.log("destination url: " +destinationURL)
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