<?php
App::uses('AppController', 'Controller');
/**
 * Ads Controller
 *
 * @property Ad $Ad
 * @property PaginatorComponent $Paginator
 */
class AdsController extends AppController {

/**
 * Components
 *
 * @var array
 */
	public $components = array('Paginator','RequestHandler');
	
/**
 * index method
 *
 * @return void
 */
	public function index() {
		$this->Ad->recursive = 0;
		$this->set('ads', $this->Paginator->paginate());
	}
	
	public function indexjson() {
		$this->autoRender=false;
		$this->Ad->recursive = 0;
		$ads=$this->Ad->find('all');
		return json_encode(compact('ads'));
	}
	
	
	public function allads($id) {
		
	}
	
	 
	
/**
 * view method
 *
 * @throws NotFoundException
 * @param string $id
 * @return void
 */
	public function view($id = null) {
		if (!$this->Ad->exists($id)) {
			throw new NotFoundException(__('Invalid ad'));
		}
		$options = array('conditions' => array('Ad.' . $this->Ad->primaryKey => $id));
		$this->set('ad', $this->Ad->find('first', $options));
	}
	public function getad($id = null) {
		$this->Ad->recursive = 0;
		$this->autoRender=false;
		if (!$this->Ad->exists($id)) {
			throw new NotFoundException(__('Invalid ad'));
		}
		$options = array('conditions' => array('Ad.' . $this->Ad->primaryKey => $id));
		$ad=$this->Ad->find('first', $options);
		return json_encode(compact('ad'));
	}
//If you need to acces this view just go to the url " websitename/ads/add"
	public function add() {
		if ($this->request->is('post')) {
			$this->Ad->create();
			if ($this->Ad->save($this->request->data)) {
				$this->Session->setFlash(__('The ad has been saved.'));
				return $this->redirect(array('action' => 'index'));
			} else {
				$this->Session->setFlash(__('The ad could not be saved. Please, try again.'));
			}
		}
		$categories = $this->Ad->Category->find('list');
		$this->set(compact('categories'));
	}


}
