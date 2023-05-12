import React, {useState, useEffect} from "react";
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { ListGroup} from "react-bootstrap";
import { Container, Divider } from 'semantic-ui-react'

function InfluencerCampaignCard({campaign, user}) {


    return(
        <div>
          <Container style={{ 
            textAlign: 'center', 
            backgroundColor: '#f8f8f8', 
            padding: '25px', 
            borderRadius: '5px', 
            boxShadow: '0px 0px 5px 0px rgba(0,0,0,0.3)',
            margin: '20',
            width: '70%',
            height: '25%',
            fontSize: '1.5em',
            display: 'flex'
          }}>
            <b>Campaign Name:</b>{campaign.name}
            <Divider />
            <b>Product Category: </b> {campaign.product_category}
            <b>Target Revenue: </b>${campaign.target_revenue}
            <b>Target Views </b>{campaign.target_views}
          </Container>
        </div>
    )
}

export default InfluencerCampaignCard;