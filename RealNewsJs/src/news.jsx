//import React from "react";
import Row from "react-bootstrap/Row";

import styled from "styled-components";

function News() {
  const LayoutMo = styled.section``;

  const Retangulo = styled.section`
    border: 1px solid red;
    min-width: 350px;
    height: 150px;
  `;

  const Img = styled.section`
    height: 90px;
    width: 90px;
    border: 0.5px solid green;
  `;

  const Titulo = styled.section`
  
  
  `;
  return (
    <>
      <LayoutMo>
        <Row>
          <Retangulo>
            <Titulo >
              <span>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin
                mollis volutpat ex
              </span>
            </Titulo>
            <Img></Img>
          </Retangulo>
        </Row>
      </LayoutMo>
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
