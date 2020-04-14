import dependency_injector.providers as providers
from ...models.main_storage_account import StorageAccount

storage_account_provider = providers.Singleton(StorageAccount)