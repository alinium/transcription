// client-side js
// run by the browser each time your view template is loaded

// protip: you can rename this to use .coffee if you prefer

// by default, you've got jQuery,
// add other scripts at the bottom of index.html

$(function() {
  console.log('hello world :o');
  
  $.get('/dreams', function(data) {
    data.dreams.forEach(function(dream) {
      console.log(dream);
    });
  });

  /*$('form').submit(function(event) {
    event.preventDefault();
    var p1 = $('#person1').val();
    var p2 = $('#person2').val();
    var sbv = $('#sbv').val();
    $.post('/dreams?' + $.param({person1: p1, person2: p2, sbv: sbv}), function() {
      //$('<li>' + dream + '</li>').appendTo('ul#dreams');
      //$('input').val('');
      //$('input').focus();
    });
  });*/

});
