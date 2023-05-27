//import React from "react";
import Row from "react-bootstrap/Row";

import styled from "styled-components";

function News() {
  const Retangulo = styled.section`
    border-radius: 5px;
    max-width: 360px;
    height: 150px;

    background: #ffffff;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);

    display: flex; 
    justify-content: space-between; 
    align-items: center; 
    margin: 20px auto;
  `;

  const Img = styled.section`
    height: 79.76px;
    min-width: 100px;
    border-radius:5px;
    border: 0.5px solid green;
    margin: 0 10px;

  `;

  const Titulo = styled.section`
  color:#8A0909;
  font-size:18px;
  margin: 0 10px;
  `;

  return (
    <>
      <Row>
        <Retangulo>
          <Img> </Img>
          <Titulo>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin
            mollis volutpat ex
          </Titulo>
        </Retangulo>
      </Row>
    </>
  );
}

export default News;

/**
 *
 *
 *
 *
 */
