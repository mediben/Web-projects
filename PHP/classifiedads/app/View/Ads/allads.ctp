<div class="adsid" idcat="<?php echo $this->request->params['pass'][0];?>">
</div>

<script type="text/javascript">
$( document ).ready(function() {
var idcat=$(".adsid").attr("idcat");

$.getJSON( "/classifiedads/categories/getadsbyid/"+idcat, function( data ) {
console.log(data);
var picture;	
  var items = [];
  $.each( data, function( key, val ) {
   $.each( val, function( key1, val1 ) {
  console.log(val1.Ad.title);
   // items.push( "<li id='" + key + "'>" + val + "</li>" );
	
	if(val1.Ad.picture){
	picture='<img class="img-responsive" src="/classifiedads/img/ads/'+val1.Ad.picture+'" />'
	}else{
	picture=' <img class="img-responsive" src="img/no-picture.jpg" alt="">';
	}
    $(".contentcat").append( '<div class="col-md-3 col-sm-6 hero-feature"><a href="/classifiedads/ads/view/'+val1.Ad.id+'">'+picture+'<div class="caption"><h3 >'+val1.Ad.title+'</h3><p class="btn btn-primary">'+val1.Ad.price+' $ </p></div></a></div>');
  });
  });
 console.log(items)
});
});
</script>