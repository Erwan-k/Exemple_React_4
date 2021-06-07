import React from 'react';

import {Button, Card} from 'react-bootstrap'

class ElementConversation extends React.Component {
	constructor(){
		super()
		this.sumbitVisualiser = this.sumbitVisualiser.bind(this)
	}

	sumbitVisualiser(){
		this.props.changerVisualiser(this.props.infos.id_conv)
	}

	render() {
		return(
			<Card>
				<Card.Body>
					<Card.Title> {this.props.infos.nom} </Card.Title>
					<Button onClick={this.sumbitVisualiser}> Visualiser </Button>
				</Card.Body>
			</Card>
		)
	}
}

export default ElementConversation;