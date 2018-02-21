<div class="adsid" idad="<?php echo $this->request->params['pass'][0];?>">
</div>

 <div class="row">
            <div class="col-md-8 pictad">
              
            </div>
            <!-- /.col-md-8 -->
            <div class="col-md-4">
                <h1 class="titlead"></h1>
                <p class="descriptionad"></p>
                <h3 class="btn-lg1" ></h3>
				<h2 style="float:right; background-color:#ccc" class="btn-lg"> Price :</h2>
            </div>
            <!-- /.col-md-4 -->
        </div>

<script type="text/javascript">
$( document ).ready(function() {
var idad=$(".adsid").attr("idad");

$.getJSON( "/classifiedads/ads/getad/"+idad, function( data ) {
console.log(data);
var picture;	
  var items = [];
  $.each( data, function( key, val ) {
   //$.each( val, function( key1, val1 ) {
  console.log(val);
   // items.push( "<li id='" + key + "'>" + val + "</li>" );
	
	if(val.Ad.picture){
	picture='<img class="img-responsive" src="/classifiedads/img/ads/'+val.Ad.picture+'" />'
	}else{
	picture=' <img class="img-responsive" src="img/no-picture.jpg" alt="">';
	}
	$(".pictad").append(picture);
	$(".titlead").append(val.Ad.title);
	$(".descriptionad").append(val.Ad.description);
	$(".btn-lg1").append(val.Ad.mail);
	$(".btn-lg").append(val.Ad.price+' $');
   // $(".contentcat").append( '<div class="col-md-3 col-sm-6 hero-feature"><a href="/classifiedads/ads/view/'+val1.Ad.id+'">'+picture+'<div class="caption"><h3 >'+val1.Ad.title+'</h3><p class="btn btn-primary">'+val1.Ad.price+' $ </p></div></a></div>');
 // });
  });
 console.log(items)
});
});
</script>