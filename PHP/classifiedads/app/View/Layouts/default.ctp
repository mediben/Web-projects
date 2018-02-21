<?php
/**
 * @link          http://cakephp.org CakePHP(tm) Project
 * @package       app.View.Layouts
 * @since         CakePHP(tm) v 0.10.0.1076
 */

?>
<!DOCTYPE html>
<html>
<head>
	<?php //echo $this->Html->charset(); ?>
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>
		<?php echo $this->fetch('title'); ?>
	</title>
	<?php
		echo $this->Html->meta('icon');

		echo $this->Html->css('bootstrap.min');
		echo $this->Html->css('3-col-portfolio.min');
		//echo $this->Html->css('bootstrap.min');
		//echo $this->fetch('meta');
		//echo $this->fetch('css');
		//echo $this->fetch('script');
	?>
	<?php
	echo $this->Html->script('jquery-1.11.0');
	echo $this->Html->script('bootstrap.min');
	?>
</head>
<body>

	<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
		  <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
             </div>
		 <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                   <li> <a href="/classifiedads/">Home</a>
				   </li>
                </ul>
            </div>
	</nav>  
	
	<div id="container">
	 	<div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Published.
				 <small>Ads</small>
                </h1>
            </div>
        </div>
		
		<div  class="row contentcat" >

			<?php echo $this->Session->flash(); ?>

			<?php echo $this->fetch('content'); ?>
		</div>
		
	</div>
	<div id="footer">
				 <div class="row">
                <div class="col-lg-12">
				<div class="well text-center">
                   Copyright &copy; Ben Taarit Mehdi 2014
					</div>
                </div>
            </div>
		</div>
	<script type="text/javascript">
$( document ).ready(function() {
$.getJSON( "/classifiedads/categories/indexjson", function( data ) {

var picture;	
  var items = [];
  $.each( data, function( key, val ) {
   $.each( val, function( key1, val1 ) {
  console.log(val1.Category.title);
   // items.push( "<li id='" + key + "'>" + val + "</li>" );
	
	
    $(".navbar-nav").append( '<li><a href="/classifiedads/ads/allads/'+val1.Category.id+'">'+val1.Category.title+'</a></li>');
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
	</body>
</html>
