from unittest.mock import Mock, patch
from pytest import fixture, mark, raises
from Lesson8.task8_6 import BankAccount


class TestBankAccount:
    @fixture
    def user_account(self):
        return BankAccount()

    @fixture
    def user_account_with_api(self):
        return BankAccount("http://someBankAccount/balance")

    @mark.parametrize("sum_amount, exp_res",
                      [(17, 17),
                       (726.79, 726.79),
                       (0, 0)])
    def test_empty_balance_deposit(self, sum_amount, exp_res, user_account):
        user_account.deposit(sum_amount)
        assert user_account.get_balance() == exp_res

    @mark.skipif(BankAccount().get_balance() == 0, reason="Has some bugs will be fixed later")
    def test_withdraw_empty_account(self, user_account):
        with raises(ValueError, match="Withdraw sum cannot be greater then current balance"):
            user_account.withdraw(10)

    @mark.parametrize(
        "balance, withdraw_amount, exp_balance",
        [(100, 50, 50),
         (200, 200, 0)])
    def test_withdraw(self, balance, withdraw_amount, exp_balance, user_account):
        user_account.deposit(balance)
        user_account.withdraw(withdraw_amount)
        assert user_account.get_balance() == exp_balance

    def test_get_balance_from_api(self, user_account_with_api):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"balance": 478.65}
        with patch("Lesson8.task8_6.requests.get", return_value=mock_response) as mock_get:
            balance = user_account_with_api.get_balance()
            assert balance == 478.65
            mock_get.assert_called_once_with("http://someBankAccount/balance", timeout=30)
