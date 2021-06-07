import React from 'react';
import axios from 'axios';

import {Button,Modal,Form,Row,Col} from 'react-bootstrap'

function Modifier_la_valeur(conv,nom_user,fonction_pour_re_render){
	console.log({token:localStorage.getItem("token"),ref_conv:conv,ref_user:nom_user})
	axios.post('http://127.0.0.1:1161/principal2', {token:localStorage.getItem("token"),ref_conv:conv,ref_user:nom_user})
	.then(response => {
		console.log(response.data)
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
			nom_user:""
		}
	}

	changeHandler = (e) => {
		this.setState({[e.target.name]: e.target.value})
	}

	submitHandler = (e) => {
		e.preventDefault()
		Modifier_la_valeur(this.props.infos.conversation_a_visualiser,this.state.nom_user,this.props.fonction_pour_re_render)
		this.setState({nom:""})
		this.props.onHide()
	}

	render(){
	const {nom_user} = this.state
		return(
		<Modal
			{...this.props}
			size="lg"
			aria-labelledby="contained-modal-title-vcenter"
			centered
		>
			<Modal.Header>
				<Modal.Title id="contained-modal-title-vcenter">
					Ajouter un utilisateur
				</Modal.Title>
			</Modal.Header> <br />

			<Modal.Body>
				<Form>
					<Form.Group as={Row} controlId="formPlaintextEmail">
						<Form.Label column sm="4">
							Nom de
						</Form.Label>
						<Col sm="8">
							<Form.Control type="text" placeholder="Nom" name="nom_user" value={nom_user} onChange={this.changeHandler} />
						</Col>
					</Form.Group>
				</Form> <br />
			</Modal.Body>
			
			<Modal.Footer>
				<Button onClick={this.submitHandler}>Ajouter</Button>
			</Modal.Footer>
		</Modal>
		)
	}
}

function PageModalAjouterUser(props){
	const [modalShow, setModalShow] = React.useState(false);
	return(
		<div class="aaaam">
			<>
				<Button variant="dark" onClick={() => setModalShow(true)}> Ajouter quelqu'un à la conversation </Button>

				<MyVerticallyCenteredModal
					show={modalShow}
					fonction_pour_re_render={props.fonction_pour_re_render}
					infos={props.infos}
					onHide={() => setModalShow(false)}
				/>
			</>
		</div>
	)
}

export default PageModalAjouterUser;














