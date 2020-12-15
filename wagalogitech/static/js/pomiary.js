$(document).ready(function(){

  console.log("pomiary ajax function")
  $.ajax({
     url: revers_urls.api_v1_pomiary,
     type: "GET",
  }).done(function (response) {
      for(i=0; i<response.length; i++){
           console.log(response[i].id)
           $('#mytable').append(
           '<tr>' +
              '<td>' + response[i].id + '</td>' +
              '<td>' + response[i].czyWazny + '</td>' +
              '<td>' + response[i].wartosc + '</td>' +
              '<td>' + response[i].data_pomiaru + '</td>' +
              '<td>' + response[i].owner + '</td>' +
              '<td>' +
                 '  <a href="' + revers_urls.front_organizacje + response[i].id + '" class="btn btn-primary btn-sm">' + response[i].id + '</a>' +
              '</td>' +
           '</tr>');
      }
  }).fail(function() {
     alert("Wystapil blad w polaczeniu z djangorestapi!")
  }).then(function() {
    $('#mytable').dataTable( {
      "order": [[ 3, "desc" ]]
    });
  })

})