$.get('http://swapi.co/api/films?format=json', function (data, textStatus) {
  data.results.map(function (x) {
    $('#list_movies').append('<li>' + x.title + '</li>');
  });
});
