<script type="text/javascript">
$( document ).ready(function() {
$.getJSON( "categories/indexjson", function( data ) {

var picture;	
  var items = [];
  $.each( data, function( key, val ) {
   $.each( val, function( key1, val1 ) {
  console.log(val1.Category.title);
   // items.push( "<li id='" + key + "'>" + val + "</li>" );
	
	if(val1.Category.picture){
	picture='<img class="img-responsive" src="img/categories/'+val1.Category.picture+'" />'
	}else{
	picture=' <img class="img-responsive" src="img/no-picture.jpg" alt="">';
	}
    $(".contentcat").append( '<div class="col-md-4 portfolio-item"><a href="ads/view/'+val1.Category.id+'">'+picture+' <h3>'+val1.Category.title+'</h3></a></div>');
  });
  });
 console.log(items)
 /* $( "<div/>", {
    "class": "col-md-4 portfolio-item",
    html: items.join( "" )
  }).appendTo( ".contentcat" );*/
});
});
</script>