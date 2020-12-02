$(document).ready(function(){

  console.log("pomiary ajax function")
  $.ajax({
     url: "http://127.0.0.1:8000/api/v1/pomiary/",
     type: "GET",
  }).done(function (response) {
      for(i=0; i<response.length; i++){
           console.log(response[i].id)
           $('#mytable').append(
           '<tr>' +
              '<td>' + response[i].id + '</td>' +
              '<td>' + response[i].owner + '</td>' +
              '<td>' + response[i].czyWazny + '</td>' +
              '<td>' + response[i].wartosc + '</td>' +
              '<td>' + response[i].data_pomiaru + '</td>' +
              '<td>' +
                 '  <a href="/front/pomiary/' + response[i].id + '" class="btn btn-primary btn-sm">' + response[i].id + '</a>' +
              '</td>' +
           '</tr>');
      }
  }).fail(function() {
     alert("Wystapil blad w polaczeniu z djangorestapi!")
  })

})