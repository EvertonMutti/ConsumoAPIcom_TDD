<h1>Consumo de API orientado a TDD</h1>
<h2>Este projeto tem o intuito de consumir a API do github e coletar dados do usuário a partir do seu username com o Desenvolvimento Orientado por Testes(TDD)</h2>

<h2>Requisitos:</h2>
<p>pip install unittest</p>
<p>pip install requests </p>

<h2>Como usar:</h2>
<br>
<p>Crie um objeto a partir da classe User passando como parâmetro o username do usuário.</p>
<br>
<code>
    from user.user import User
    
    usuario = User('EvertonMutti')
</code>
<p>Ao ser instanciado, os seguintes atributos são criados:</p>
<p>username(string), username do usuário no Github.</p>
<p>nome(string), nome do usuário do Github.</p>
<p>url_perfil(string), url do perfil do usuário no Github.</p>
<p>num_repos_publicos(int), número de repositórios públicos do usuário.</p>
<p>num_seguidores(int), número de seguidores do usuário.</p>
<p>num_seguindo(int), número de usuários que o usuário segue.</p>
<br>
<h2>Métodos</h2>
<br>
<p>obterDados(): obtém os dados do usuário a partir do username passado na inicialização da classe e para acessar as informações que ele coleta, acesse os atributos listados acima</p>
<p>obterRepositorios(): obtém os repositórios do usuário a partir do username passado na inicialização da classe</p>
<p>gerarArquivo(): obtém os repositórios e dados do usuário os transferindo para um arquivo txt com o nome do username passado na inicialização do objeto.</p> 

<h2>Testes</h2>
<p>Os testes verificam se os atributos da classe estão sendo criados corretamente, se a verificação do código de resposta da API do Github está funcionando corretamente e se os métodos como obterDados(), obterRepositorios(), gerarArquivo() estão funcionando corretamente</p>

    
    