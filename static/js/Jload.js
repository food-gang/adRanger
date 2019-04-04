var loadGoods = function(){
        /* загрузка товаров на страницу */
        var request = new XMLHttpRequest();
        request.open('GET', 'statc/js/data_file.json', true);
        console.log(request)
        request.onload = function() {
        if (request.status >= 200 && request.status < 400) {
            // Success!
            console.log('request is ok!')
            var data = JSON.parse(request.responseText);
            var outJson = "";
            for (var key in data) {
                if (data.hasOwnProperty(key)) {
                    outJson += "<div class='item'>;"
                    outJson += "<img width='100px' src='" +data[key].url+ "'>";
                    outJson += "<p class='namesp'> " +data[key].name+ ".</p>";
                    outJson += "<p>" +data[key].price+ "</p>";
                    outJson += "<p>" +data[key].place+ ".</p>";
                    outJson +="<button><a href='"+data[key].ref+"> Купить</a></button>"
                    outJson += "</div>";
                }
            }
            console.log(outJson)
            goods.innerHTML = outJson;
            //console.log(goods)

        } else {
            // We reached our target server, but it returned an error
            console.log('hule ne chitaetsa')
        }
        };

        request.onerror = function() {
        // There was a connection error of some sort
        };

        request.send();
    };
    loadGoods();﻿
$(function(){
  $('#post').html('sosi bibu lox');
});
