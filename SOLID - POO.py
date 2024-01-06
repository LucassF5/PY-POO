"""

 SOLID é um conjunto de cinco princípios de design de software que visam criar código mais compreensível, 
 flexível e fácil de manter. Esses princípios foram introduzidos por Robert C. Martin 
 e são frequentemente utilizados na Programação Orientada a Objetos (POO). 
 Vamos dar uma breve visão geral de cada princípio e como eles podem ser aplicados em Python:

# 1. Princípio da Responsabilidade Única (SRP): 
 Uma classe deve ter apenas um motivo para mudar. 
 Certifique-se de que suas classes e métodos realizem tarefas específicas e tenham uma única responsabilidade. 
 Isso facilita a manutenção e compreensão do código.

# 2. Princípio Aberto/Fechado (OCP): 
 Uma classe deve estar aberta para extensão, mas fechada para modificação. 
 Use herança e polimorfismo para permitir a extensão sem modificar o código existente. 
 Utilize interfaces e classes abstratas para definir contratos que podem ser estendidos.

# 3. Princípio da Substituição de Liskov (LSP): 
 Os objetos de uma classe derivada devem ser capazes de substituir os objetos de sua classe base sem afetar a integridade do programa. 
 Certifique-se de que as subclasses possam ser usadas em qualquer lugar onde a classe base é usada, mantendo a consistência do programa.

# 4. Princípio da Segregação de Interface (ISP): 
 Nenhuma classe deve ser forçada a implementar métodos que ela não utiliza. 
 Divida interfaces grandes em interfaces menores e mais específicas. 
 Isso evita que as classes implementem métodos desnecessários.

# 5. Princípio da Inversão de Dependência (DIP): 
 Módulos de alto nível não devem depender de módulos de baixo nível. 
 Ambos devem depender de abstrações. Utilize injeção de dependência e interfaces para inverter as dependências. 
 Isso torna o código mais flexível e menos acoplado.

 Ao aplicar os princípios SOLID em Python, você promove um design de código mais robusto, 
 fácil de estender e menos propenso a erros durante a evolução do software. 
 Esses princípios incentivam a criação de sistemas mais modularizados e flexíveis, 
 fundamentais para o desenvolvimento sustentável de software em Python ou qualquer outra linguagem orientada a objetos.

"""