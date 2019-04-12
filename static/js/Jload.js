
//loadGoods()
/*var loadGoods=function(){
  $.getJSON('/static/js/data_file.json', function(data){
  var items = [];

  $.each(data, function(key, val){
    items.push('<li id="' + data[key] + '">' + data[val] + '</li>');
  });
  console.log(items)
  $('<ul/>', {
    'class': 'my-new-list',
    html: items.join('')
  }).appendTo('#post');
});
}*/
function loadGoods() {
    //загружаю товары на страницу
    $.getJSON('/static/js/data_file.json', function (data) {
        //console.log(data);
        var out = '';
        for (var key in data){
            out+='<div class="col-lg-3 col-md-6 pr1">';
            out+='<div class="imagehere">';
            out+='<img width=205px; height=205px; src="'+data[key].url+'" alt="photo">';
            out+='</div>';
            out+='<div class="text-center">';
            out+='<h5><a href="'+data[key]['ref']+'"target="_blank">'+data[key]['name']+'</a></h5>';
            out+='<h6>Цена:'+data[key]['price']+'</h6>';
            out+='</div>';
            out+='</div>';
        }
        $('#row').html(out);
    })
}
loadGoods();
/*window.onload = function() {
  var x= document.getElementById("search");
  x.onclick=loadGoods();
  //x.onclick=  window.location.reload();
}*/

//document.getElementById("Search").onclick = loadGoods;
//document.getElementById("Search").onclick = function () { alert('hello!'); };
