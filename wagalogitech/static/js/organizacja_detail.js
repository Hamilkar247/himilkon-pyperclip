//wartosci z bazy danych pewnej organizacji
$(document).ready(function(){
   console.log("jestesmy w szczegolach organizacji"),
   $.ajax({
      url: "http://127.0.0.1:8000/api/organizacje/1", //do poprawienia !!!
      type: "GET",
   }).done(function(response) {
       console.log("udalo sie pobrac z ajaksa dane !")
       $('#nazwa_organizacji').attr('value', response.nazwa);
       $("#opis_organizacji").attr('value', response.opis);
   }).fail(function() {
     alert("Wystąpił błąd w połączeniu z djangorestapi!");
   })
})