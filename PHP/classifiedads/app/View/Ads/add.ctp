<div class="ads form">
<?php echo $this->Form->create('Ad'); ?>
	<fieldset>
	<?php
		echo $this->Form->input('title');
		echo $this->Form->input('description');
		echo $this->Form->input('price');
		echo $this->Form->input('mail');
		?>
		<h5 style="color:red">Please insert the image name only (exemple.jpg) and add it to your folder <strong>ads</strong></h5>
		<?php
		
		echo $this->Form->input('picture');
		echo $this->Form->input('categories_id');
	?>
	</fieldset>
<?php echo $this->Form->end(__('Submit')); ?>
</br>
</div>

