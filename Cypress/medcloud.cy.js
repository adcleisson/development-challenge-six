describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://qa.medcloud.link/')
      let time1 = 500
      let time2 = 1000


      cy.wait(time1)
      cy.contains('button', 'Aceitar').click()


      cy.get('#headerRis').click()
      cy.wait(time1)
      cy.get('#headerPacs').click()
      cy.wait(time1)
      cy.get('#headerPortal').click()
      cy.wait(time1)
      cy.get('#headerPlans').click()
      cy.wait(time1)
      cy.get('#headerContact').click()
      cy.wait(time1)

      cy.get('input[placeholder="Informe seu nome"]').eq(1).type('João da Silva')
      cy.get('input[placeholder="Informe seu e-mail"]').eq(1).type('teste@gmail.com')
      cy.get('input[placeholder="Informe seu telefone"]').eq(1).type('(42)999999999')
      cy.get('#message').type('Olá, tudo bem?')
      cy.contains('button', 'Enviar').should('be.visible').click()

      cy.wait(time1)
      cy.contains('button', 'Inglês').click()
      cy.wait(time1)
      cy.contains('button', 'Portugués - BR').click()
      cy.wait(time1)
      cy.contains('button', 'Espanhol').click()
      cy.wait(time1)
      cy.contains('button', 'Portugués - BR').click()


      cy.contains('a', 'Sobre').click()
      cy.wait(time2)
      cy.get('img[alt="back"]').parent('a').click()

      cy.contains('a', 'Carreiras').click()
      cy.contains('h3', 'Analista de RH').click()

      cy.get('input[placeholder="Informe seu sobrenome"]').type('Silva')
      cy.wait(time2)
      cy.get('input[placeholder="Informe seu e-mail"]').type('jssilva@gmail.com')
      cy.wait(time2)
      cy.get('input[placeholder="Informe seu telefone"]').type('(11)999999999')
      cy.wait(time2)
      cy.get('#message').type('Olá a todos, me chamo Jõao da Silva Sauro Silva...')
      cy.get('img[alt="back"]').parent('a').click()
      cy.wait(time1)
      cy.get('img[alt="back"]').parent('a').click()
      cy.wait(time1)



  })
})