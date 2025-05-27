import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Defina o token de acesso do Slack
slack_token = 'xoxp-your-slack-token'
client = WebClient(token=slack_token)

def update_user_profile(user_id, new_display_name):
    try:
        # Atualiza o perfil do usuário
        response = client.users_profile_set(
            user=user_id,
            profile={
                'display_name': new_display_name
            }
        )
        print(f"Perfil atualizado: {response['profile']['display_name']}")
    except SlackApiError as e:
        print(f"Erro ao atualizar o perfil: {e.response['error']}")

def get_user_id(user_name):
    try:
        # Obtém a lista de usuários
        response = client.users_list()
        users = response['members']

        # Procura o ID do usuário pelo nome
        for user in users:
            if user['name'] == user_name:
                return user['id']
        return None
    except SlackApiError as e:
        print(f"Erro ao obter a lista de usuários: {e.response['error']}")
        return None

if __name__ == "__main__":
    # Nome de usuário sem emojis
    user_name = 'raphael.barbosa'
    # Emojis a serem adicionados
    whale_emoji = ':whale:'
    lgbt_flag_emoji = ':rainbow_flag:'

    # Obtém o ID do usuário
    user_id = get_user_id(user_name)
    if user_id:
        # Constrói o novo display name com os emojis
        new_display_name = f"{user_name} {whale_emoji} {lgbt_flag_emoji}"
        # Atualiza o perfil do usuário
        update_user_profile(user_id, new_display_name)
    else:
        print(f"Usuário {user_name} não encontrado")