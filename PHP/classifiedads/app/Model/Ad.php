<?php
App::uses('AppModel', 'Model');

class Ad extends AppModel 
{
	public $belongsTo = array(
		'Category' => array(
			'className' => 'Categories',
			'foreignKey' => 'categories_id',
			'conditions' => '',
			'fields' => '',
			'order' => ''
		)
	);
}
