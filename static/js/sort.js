 document.querySelector('#sort-asc').onclick = mySort();
 document.querySelector('#sort-desc').onclick = mySortDec();
console.log('etot shit hotya bi zapuskaetsa')
function mySort() {
  var rpr1 = document.querySelector('#rpr1');
  for(var i = 0; i < rpr1.children.length; i++){
    for(var j = i; j < rpr1.children.length; j++){
      if(+rpr1.children[i].getAttribute('data-price') > +rpr1.children[j].getAttribute('data-price')){
        replacedNode = rpr1.replaceChild(rpr1.children[j], rpr1.children[i]);
        insertAfter(replacedNode, rpr1.children[i]);
      }
    }
  }
}
mySort();
function mySortDec() {
  var rpr1 = document.querySelector('#rpr1');
  for(var i = 0; i < rpr1.children.length; i++){
    for(var j = i; j < rpr1.children.length; j++){
      if(+rpr1.children[i].getAttribute('data-price') < +rpr1.children[j].getAttribute('data-price')){
        replacedNode = rpr1.replaceChild(rpr1.children[j], rpr1.children[i]);
        insertAfter(replacedNode, rpr1.children[i]);
      }
    }
  }
}

function insertAfter(elem, refElem){
  return refElem.parentNode.insertBefore(elem, refElem.nextSibling);
}
