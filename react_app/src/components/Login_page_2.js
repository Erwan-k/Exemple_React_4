import React from 'react';
import axios from 'axios';
import {Form,Row,Col,Button} from 'react-bootstrap'


class Login_page_2 extends React.Component {
	constructor(){
		super()
		this.state = {
			adresse_mai:"",
			mot_de_passe:"",
			nom:"",
      retour_api:""
		}
	}

	changeHandler = (e) => {
		this.setState({[e.target.name]: e.target.value})
	}

	submitHandler = (e) => {
		e.preventDefault()
    axios.post('http://127.0.0.1:1161/connexion1',{
    												adresse_mail:this.state.adresse_mai,
    												mot_de_passe:this.state.mot_de_passe,
    												nom:this.state.nom
    											})
        .then(response => {
            if(response.status === 200){
                console.log(response)
                this.setState({retour_api:response.data.retour})
                if (response.data.retour === "ok"){
                  this.setState({adresse_mai:"",mot_de_passe:"",nom:""})
                                                  }
                                       }
                          }
              ).catch(error => {console.log(error)})
	}

	render() {
  	const {adresse_mai,mot_de_passe,nom,retour_api} = this.state
  	return(
      <div class="login-page-1-1">
        <div class="login-page-1-2">
            <Form onSubmit={this.submitHandler}>
              <Form.Group as={Row} controlId="formHorizontalEmail">
                <Form.Label column sm={2}>
                  Adresse mail 
                </Form.Label>
                <Col sm={10}>
                  <Form.Control type="email" placeholder="Adresse mail" name="adresse_mai"  value={adresse_mai} onChange={this.changeHandler}/>
                </Col>
              </Form.Group>

              <Form.Group as={Row} controlId="formHorizontalPassword">
                <Form.Label column sm={2}>
                  Nom
                </Form.Label>
                <Col sm={10}>
                  <Form.Control type="text" placeholder="Nom" name="nom" value={nom} onChange={this.changeHandler} />
                </Col>
              </Form.Group>

              <Form.Group as={Row} controlId="formHorizontalPassword">
                <Form.Label column sm={2}>
                  Mot de passe
                </Form.Label>
                <Col sm={10}>
                  <Form.Control type="text" placeholder="Mot de passe" name="mot_de_passe" value={mot_de_passe} onChange={this.changeHandler} />
                </Col>
              </Form.Group>

              <Form.Group as={Row}>
                <Col sm={{ span: 10, offset: 2 }}>
                  <Button type="submit">S'inscrire</Button>
                </Col>
              </Form.Group>
            </Form>

            {retour_api}

        </div>
      </div>
    	)
    }
}

export default Login_page_2;


