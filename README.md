<h1>Consumo de API orientado a TDD</h1>
<h2>Este projeto tem o intuito de consumir a API do github e coletar dados do usuário a partir do seu username com o Desenvolvimento Orientado por Testes(TDD)</h2>

<h2>Requisitos:</h2>
<code>pip install unittest</code>
<br>
<code>pip install requests</code>

<h2>Como usar:</h2>
<br>
<p>Crie um objeto a partir da classe User passando como parâmetro o username do usuário.</p>

<code>from user.user import User</code>
<br>
<code>usuario = User('EvertonMutti')</code>
<br>
<p>Ao ser instanciado, os seguintes atributos são criados:</p>
<p><b>username(string)</b>, username do usuário no Github.</p>
<p><b>nome(string)</b>, nome do usuário do Github.</p>
<p><b>url_perfil(string)</b>, url do perfil do usuário no Github.</p>
<p><b>num_repos_publicos(int)</b>, número de repositórios públicos do usuário.</p>
<p><b>num_seguidores(int)</b>, número de seguidores do usuário.</p>
<p><b>num_seguindo(int)</b>, número de usuários que o usuário segue.</p>
<br>
<h2>Métodos</h2>
<br>
<p><b>obterDados()</b>: obtém os dados do usuário a partir do username passado na inicialização da classe e para acessar as informações que ele coleta, acesse os atributos listados acima.</p>
<p><b>obterRepositorios()</b>: obtém os repositórios do usuário a partir do username passado na inicialização da classe.</p>
<p><b>gerarArquivo()</b>: obtém os repositórios e dados do usuário os transferindo para um arquivo txt com o nome do username passado na inicialização do objeto.</p> 

<h2>Testes</h2>
<p>Os testes verificam se os atributos da classe estão sendo criados corretamente, se a verificação do código de resposta da API do Github está funcionando corretamente e se os métodos como obterDados(), obterRepositorios(), gerarArquivo() estão funcionando corretamente</p>

    
    
