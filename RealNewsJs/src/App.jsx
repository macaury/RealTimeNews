/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import React from "react";
import Row from "react-bootstrap/Row";

import styled from "styled-components";

function App() {
  const Button = styled.button`
    background: ${props => (props.$primary ? "#BF4F74" : "white")};
    color: ${props => (props.$primary ? "white" : "#BF4F74")};

    font-size: 1em;
    margem: 0.5rem;
    border: 2px solid #bf4f74;
    border-radius: 3px;
  `;

  const Tesmato = styled(Button)`
    background: pink;
    width: 100%;
  `;
  const Layout_main = styled.section`
   
  `;
  const Test_container = styled.section `
  
`;

  return (
    <>
      <Test_container>
        <Layout_main>
          <Row>
            <div>
              <Button>Normal</Button>
              <Button $primary>Primary</Button>
              <Tesmato></Tesmato>
            </div>
          </Row>
        </Layout_main>
      </Test_container>
    </>
  );
}

export default App;

/** 
 * 
 * 
 * 
 *  max-width: 480px;
    min-width: 320px;
    align:center;
    position:absolute;
 */