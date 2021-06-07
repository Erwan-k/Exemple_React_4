import React from 'react';
import axios from 'axios';

import {Button,Modal,Form,Row,Col} from 'react-bootstrap'

function Modifier_la_valeur(nom,fonction_pour_re_render){
	axios.post('http://127.0.0.1:1161/principal1', {token:localStorage.getItem("token"),nom_conv:nom})
	.then(response => {
		if(response.status === 200){
			if (response.data.retour === "ok"){
				fonction_pour_re_render()
			}
		}
	})
	.catch(error => {console.log(error)})
}

class MyVerticallyCenteredModal extends React.Component{
	constructor(){
		super()
		this.state = {
			nom:""
		}
	}

	changeHandler = (e) => {
		this.setState({[e.target.name]: e.target.value})
	}

	submitHandler = (e) => {
		e.preventDefault()
		Modifier_la_valeur(this.state.nom,this.props.fonction_pour_re_render)
		this.setState({nom:""})
		this.props.onHide()
	}

	render(){
	const {nom} = this.state
		return(
		<Modal
			{...this.props}
			size="lg"
			aria-labelledby="contained-modal-title-vcenter"
			centered
		>
			<Modal.Header>
				<Modal.Title id="contained-modal-title-vcenter">
					Nouvelle conversation
				</Modal.Title>
			</Modal.Header> <br />

			<Modal.Body>
				<Form>
					<Form.Group as={Row} controlId="formPlaintextEmail">
						<Form.Label column sm="4">
							Nom
						</Form.Label>
						<Col sm="8">
							<Form.Control type="text" placeholder="Nom" name="nom" value={nom} onChange={this.changeHandler} />
						</Col>
					</Form.Group>
				</Form> <br />
			</Modal.Body>
			
			<Modal.Footer>
				<Button onClick={this.submitHandler}>Créer</Button>
			</Modal.Footer>
		</Modal>
		)
	}
}

function PageModalAjouter(props){
	const [modalShow, setModalShow] = React.useState(false);
	return(
		<div class="aaaah">
			<>
				<Button variant="dark" onClick={() => setModalShow(true)}> Créer une conversation </Button>

				<MyVerticallyCenteredModal
					show={modalShow}
					fonction_pour_re_render={props.fonction_pour_re_render}
					onHide={() => setModalShow(false)}
				/>
			</>
		</div>
	)
}

export default PageModalAjouter;














