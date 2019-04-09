
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
            out+='<div class="item">';
            out+='<h3>'+data[key]['name']+'</h3>';
            out+='<p>Цена: '+data[key]['price']+'</p>';
            out+='<img src="'+data[key].url+'">';
            out+="<button><a href='"+data[key].ref+"'> Купить</a></button>";
            out+='</div>';
        }
        $('#post').html(out);
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
