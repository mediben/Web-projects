<div class="ads index">
	<h2><?php echo __('Ads'); ?></h2>
	<table cellpadding="0" cellspacing="0">
	<thead>
	<tr>
			<th><?php echo $this->Paginator->sort('id'); ?></th>
			<th><?php echo $this->Paginator->sort('title'); ?></th>
			<th><?php echo $this->Paginator->sort('description'); ?></th>
			<th><?php echo $this->Paginator->sort('price'); ?></th>
			<th><?php echo $this->Paginator->sort('mail'); ?></th>
			<th><?php //echo $this->Paginator->sort('picture'); ?></th>
			<th><?php //echo $this->Paginator->sort('categories_id'); ?></th>
			<th class="actions"><?php echo __('Actions'); ?></th>
	</tr>
	</thead>
	<tbody>
	<?php foreach ($ads as $ad): ?>
	<tr>
		<td><?php echo h($ad['Ad']['id']); ?>&nbsp;</td>
		<td><?php echo h($ad['Ad']['title']); ?>&nbsp;</td>
		<td><?php echo h($ad['Ad']['description']); ?>&nbsp;</td>
		<td><?php echo h($ad['Ad']['price']); ?>&nbsp;</td>
		<td><?php echo h($ad['Ad']['mail']); ?>&nbsp;</td>
		<td><?php //echo h($ad['Ad']['picture']); ?>&nbsp;</td>
		<td>
			<?php //echo $this->Html->link($ad['Categories']['title'], array('controller' => 'categories', 'action' => 'view', $ad['Categories']['id'])); ?>
		</td>
		<td class="actions">
			<?php echo $this->Html->link(__('View'), array('action' => 'view', $ad['Ad']['id'])); ?>
		</td>
	</tr>
<?php endforeach; ?>
	</tbody>
	</table>
	<p>
	<?php
	echo $this->Paginator->counter(array(
	'format' => __('Page {:page} of {:pages}, showing {:current} records out of {:count} total, starting on record {:start}, ending on {:end}')
	));
	?>	</p>
	<div class="paging">
	<?php
		echo $this->Paginator->prev('< ' . __('previous'), array(), null, array('class' => 'prev disabled'));
		echo $this->Paginator->numbers(array('separator' => ''));
		echo $this->Paginator->next(__('next') . ' >', array(), null, array('class' => 'next disabled'));
	?>
	</div>
</div>

