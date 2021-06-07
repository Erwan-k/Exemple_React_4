import React from 'react';
import axios from 'axios';
import {Redirect} from 'react-router-dom';
import {Form,Row,Col,Button} from 'react-bootstrap'

class Login_page_1 extends React.Component {
	constructor(){
		super()

    let logged_temp
    if (localStorage.getItem("logged") === null) {
      logged_temp = false
      localStorage.setItem("logged",false)
      localStorage.setItem("eleve_ou_conteneur","eleve")
    }
    else {logged_temp = localStorage.getItem("logged")}

		this.state = {
			adresse_mail:"",
			mot_de_passe:"",
      retour_api:"",
      logged: logged_temp
		}
	}

	changeHandler = (e) => {
		this.setState({[e.target.name]: e.target.value})
	}

	submitHandler = (e) => {
		e.preventDefault()
    axios.post('http://127.0.0.1:1161/connexion7',{adresse_mail:this.state.adresse_mail,mot_de_passe:this.state.mot_de_passe})
        .then(response => {
            if(response.status === 200){
                this.setState({retour_api:response.data.retour})
                if (response.data.retour === "ok"){
                  localStorage.setItem("token",response.data.token)
                  localStorage.setItem("logged",true)
                  this.setState({logged:true})
                                          }
                                       }
                          }
              ).catch(error => {console.log(error)})
	}

	render() {
  	const {adresse_mail,mot_de_passe,retour_api,logged} = this.state
    if (logged === true) {return <Redirect to="/page_principale/" />}

  	return(
    	<div class="login-page-1-1">
        <div class="login-page-1-2">
            <Form onSubmit={this.submitHandler}>
              <Form.Group as={Row} controlId="formHorizontalEmail">
                <Form.Label column sm={2}>
                  Adresse mail 
                </Form.Label>
                <Col sm={10}>
                  <Form.Control type="email" placeholder="Adresse mail" name="adresse_mail"  value={adresse_mail} onChange={this.changeHandler}/>
                </Col>
              </Form.Group>

              <Form.Group as={Row} controlId="formHorizontalPassword">
                <Form.Label column sm={2}>
                  Mot de passe
                </Form.Label>
                <Col sm={10}>
                  <Form.Control type="password" placeholder="Mot de passe" name="mot_de_passe" value={mot_de_passe} onChange={this.changeHandler} />
                </Col>

              </Form.Group>

              <Form.Group as={Row}>
                <Col sm={{ span: 10, offset: 2 }}>
                  <Button type="submit">Connexion</Button>
                </Col>
              </Form.Group>
            </Form>

            {retour_api}

            <div class="login-page-1-3">
              <div class="login-page-1-4">
                <p>
                  <a href="/verif_mail"> Renvoyer un email de confirmation ? </a> <br/>
                  <a href="/verif_mail"> Vérifier son adresse mail ? </a> <br/>
                </p>
              </div>
              <div class="login-page-1-4">
                <p>
                  <a href="/gestion_mdp"> Demander un code pour changer son mot de passe ? </a> <br/>
                  <a href="/gestion_mdp"> Changer son mot de passe à l'aide d'un code ? </a> <br/>
                  <a href="/gestion_mdp"> Changer son mot de passe connaissant le mot de passe actuel ? </a> 
                </p>
              </div>
            </div>

        </div>
      </div>
    	)
    }
}

export default Login_page_1;


