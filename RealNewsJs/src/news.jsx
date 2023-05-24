/* eslint-disable no-unexpected-multiline */
/* eslint-disable react/prop-types */
// eslint-disable-next-line no-unused-vars
import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";


import styled from "styled-components";

function News() {
  const Button = styled.button`
   
    background: ${props => (props.$primary ? "#BF4F74" : "white")};
    color: ${props => (props.$primary ? "white" : "#BF4F74")};

    font-size: 1em;
    margin: 1em;
    padding: 0.25em 1em;
    border: 2px solid #bf4f74;
    border-radius: 3px;
  `;

  const Tesmato = styled(Button)
  `
  color: orange;
  border-color: black;
  background:pink;
  
  `;


  return (
    <>
      <Container fluid>
        <Row>
          <div>
            <Button>Normal</Button>
            <Button $primary>Primary</Button>
            <Tesmato>Tesmato</Tesmato>
          </div>
        </Row>
      </Container>
    </>
  );
}

export default News;
