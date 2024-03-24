__all__ = [
    'Name',
    'PersonalAcc',
    'BankName',
    'BIC',
    'CorrespAcc',
    'Sum',
    'Puprose',
    'PayeeINN',
    'PayerINN',
    'DrawerStatus',
    'KPP',
    'CBC',
    'OKTMO',
    'PaytReason',
    'TaxPeriod',
    'DocNo',
    'DocDate',
    'TaxPaytKind',
    'LastName',
    'FirstName',
    'MiddleName',
    'PayerAddress',
    'PersonalAccount',
    'DocIdx',
    'PensAcc',
    'Contract',
    'PersAcc',
    'Flat',
    'Phone',
    'PayerIdType',
    'PayerIdNum',
    'ChildFio',
    'BirthDate',
    'PaymTerm',
    'PaymPeriod',
    'Category',
    'ServiceName',
    'CounterId',
    'CounterVal',
    'QuittId',
    'QuittDate',
    'InstNum',
    'ClassNum',
    'SpecFio',
    'AddAmount',
    'RuleId',
    'ExecId',
    'RegType',
    'UIN',
    'TechCode',
]

# ruff: noqa: N802, E501

from typing import Any


class RequisiteValidationError(Exception):
    pass


def max_len(value: str, maxlength: int) -> bool:
    return len(value) <= maxlength


def min_max_len(value: str, minlength: int, maxlength: int) -> bool:
    return minlength <= len(value) <= maxlength


def cast(value: Any, type_: type[str] | type[int]) -> str | int:
    return value if isinstance(value, type_) else type_(value)


def unstring_float(value: Any) -> float | str:
    """
    If float or "float in str" (f.e. 0.1 or "0.1"), returns float,
    else converts value to str then returns converted value.

    """
    if isinstance(value, float):
        return value
    try:
        is_float = bool(float(value) % 1)  # % 1 prevents int -> float
    except ValueError:
        is_float = False
    return float(value) if is_float else str(value)


def digits_only(value: str) -> str:
    return ''.join(i for i in value if i.isdigit())


def make_non_empty(value: Any) -> str:
    value = cast(value, str)
    return value or 'Не указано'


def Name(name: Any) -> str:
    name = cast(name, str)
    if not min_max_len(name, 1, 160):
        raise RequisiteValidationError(
            'ГОСТ § 5.2.3, Таблица 2: Наименование получателя платежа — '
            f'Строка от 1 до 160 знаков. Вы передали Name {name!r}, знаков: {len(name)}'
        )
    return name


def PersonalAcc(personalacc: Any) -> str:
    personalacc = cast(personalacc, str)
    personalacc = digits_only(personalacc)
    if len(personalacc) != 20:
        raise RequisiteValidationError(
            'ГОСТ § 5.2.3, Таблица 2: Номер счета получателя платежа — '
            'Строка цифр строго 20 знаков. Вы передали '
            f'PersonalAcc {personalacc!r}, знаков: {len(personalacc)}'
        )
    return personalacc


def BankName(bankname: Any) -> str:
    bankname = cast(bankname, str)
    if not min_max_len(bankname, 1, 45):
        raise RequisiteValidationError(
            'ГОСТ § 5.2.3, Таблица 2: Наименование банка получателя платежа — '
            'Строка от 1 до 45 знаков. Вы передали '
            f'BankName {bankname!r}, знаков: {len(bankname)}'
        )
    return bankname


def BIC(bic: Any) -> str:
    bic = cast(bic, str)
    bic = digits_only(bic)
    if len(bic) != 9:
        raise RequisiteValidationError(
            'ГОСТ § 5.2.3, Таблица 2: БИК — '
            'Строка цифр строго 9 знаков. Вы передали '
            f'BIC {bic!r}, знаков: {len(bic)}'
        )
    return bic


def CorrespAcc(correspacc: Any) -> str:
    if not correspacc:
        raise RequisiteValidationError(
            'ГОСТ § 5.2.3, Таблица 2: При отсутствии у банка получателя платежа '
            'корр. счета поле заполнять значением «0». Вы передали '
            f'CorrespAcc {correspacc!r}.'
        )
    correspacc = cast(correspacc, str)
    correspacc = digits_only(correspacc)
    if not max_len(correspacc, 20):
        raise RequisiteValidationError(
            'ГОСТ § 5.2.3, Таблица 2: Номер кор./сч. банка получателя платежа — '
            'Строка цифр до 20 знаков. Вы передали '
            f'CorrespAcc {correspacc!r}, знаков: {len(correspacc)}'
        )
    return correspacc


def Sum(sum_: Any) -> str:
    sum_ = unstring_float(sum_)
    if isinstance(sum_, float):
        sum_ = f'{sum_:.2f}'.replace('.', '')
    else:
        sum_ = cast(sum_, str)
        sum_ = digits_only(sum_)
    if not min_max_len(sum_, 1, 18):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: Сумма платежа, в копейках — '
            f'Макс. 18 знаков. Вы передали Sum {sum_!r}, знаков: {len(sum_)}'
        )
    return sum_


def Puprose(puprose: Any) -> str:
    puprose = cast(puprose, str)
    if not max_len(puprose, 210):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: Наименование платежа (назначение) — '
            f'Макс. 210 знаков. Вы передали Puprose {puprose!r}, знаков: {len(puprose)}'
        )
    return puprose


def PayeeINN(payeeinn: Any) -> str:
    payeeinn = cast(payeeinn, str)
    payeeinn = digits_only(payeeinn)
    if not max_len(payeeinn, 12):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: ИНН получателя платежа — '
            f'Макс. 210 знаков. Вы передали PayeeINN {payeeinn!r}, знаков: {len(payeeinn)}'
        )
    return payeeinn


def PayerINN(payerinn: Any) -> str:
    payerinn = cast(payerinn, str)
    payerinn = digits_only(payerinn)
    if not max_len(payerinn, 12):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: ИНН плательщика — '
            f'Макс. 210 знаков. Вы передали PayerINN {payerinn!r}, знаков: {len(payerinn)}'
        )
    return payerinn


def DrawerStatus(drawerstatus: Any) -> str:
    drawerstatus = cast(drawerstatus, str)
    if not max_len(drawerstatus, 2):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: Статус составителя платежного документа — '
            f'Макс. 210 знаков. Вы передали DrawerStatus {drawerstatus!r}, '
            'знаков: {len(drawerstatus)}'
        )
    return drawerstatus


def KPP(kpp: Any) -> str:
    kpp = cast(kpp, str)
    kpp = digits_only(kpp)
    if not max_len(kpp, 9):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: КПП получателя платежа — Макс. 9 знаков'
            f'Вы передали KPP {kpp!r}, знаков: {len(kpp)}'
        )
    return kpp


def CBC(cbc: Any) -> str:
    cbc = cast(cbc, str)
    cbc = digits_only(cbc)
    if not max_len(cbc, 20):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: КБК — Макс. 20 знаков'
            f'Вы передали CBC {cbc!r}, знаков: {len(cbc)}'
        )
    return cbc


def OKTMO(oktmo: Any) -> str:
    oktmo = cast(oktmo, str)
    oktmo = digits_only(oktmo)
    if not max_len(oktmo, 11):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: Общероссийский классификатор территорий '
            'муниципальных образований (ОКТМО) — Макс. 11 знаков'
            f'Вы передали OKTMO {oktmo!r}, знаков: {len(oktmo)}'
        )
    return oktmo


def PaytReason(paytreason: Any) -> str:
    paytreason = cast(paytreason, str)
    if not max_len(paytreason, 2):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: Основание налогового платежа — Макс. 2 знака. '
            f'Вы передали PaytReason {paytreason!r}, знаков: {len(paytreason)}'
        )
    return paytreason


def TaxPeriod(taxperiod: Any) -> str:
    taxperiod = cast(taxperiod, int)
    if not max_len(taxperiod, 10):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: Налоговый период — Макс. 10 знаков. '
            f'Вы передали TaxPeriod {taxperiod!r}, знаков: {len(taxperiod)}'
        )
    return taxperiod


def DocNo(docno: Any) -> str:
    docno = cast(docno, str)
    if not max_len(docno, 15):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: Номер документа – Макс. 15 знаков. '
            f'Вы передали DocNo {docno!r}, знаков: {len(docno)}'
        )
    return docno


def DocDate(docdate: Any) -> str:
    docdate = cast(docdate, str)
    if not max_len(docdate, 10):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: Дата документа – Макс. 10 знаков. '
            f'Вы передали DocDate {docdate!r}, знаков: {len(docdate)}'
        )
    return docdate


def TaxPaytKind(taxpaytkind: Any) -> str:
    taxpaytkind = cast(taxpaytkind, str)
    if not max_len(taxpaytkind, 2):
        raise RequisiteValidationError(
            'ГОСТ Таблица А.1: Дата документа – Макс. 2 знака. '
            f'Вы передали TaxPaytKind {taxpaytkind!r}, знаков: {len(taxpaytkind)}'
        )
    return taxpaytkind


def LastName(lastname: Any) -> str:
    return make_non_empty(lastname)


def FirstName(firstname: Any) -> str:
    return make_non_empty(firstname)


def MiddleName(middlename: Any) -> str:
    return make_non_empty(middlename)


def PayerAddress(payeraddress: Any) -> str:
    return make_non_empty(payeraddress)


def PersonalAccount(personalaccount: Any) -> str:
    return make_non_empty(personalaccount)


def DocIdx(docidx: Any) -> str:
    return make_non_empty(docidx)


def PensAcc(pensacc: Any) -> str:
    return make_non_empty(pensacc)


def Contract(contract: Any) -> str:
    return make_non_empty(contract)


def PersAcc(persacc: Any) -> str:
    return make_non_empty(persacc)


def Flat(flat: Any) -> str:
    return make_non_empty(flat)


def Phone(phone: Any) -> str:
    return make_non_empty(phone)


def PayerIdType(payeridtype: Any) -> str:
    return make_non_empty(payeridtype)


def PayerIdNum(payeridnum: Any) -> str:
    return make_non_empty(payeridnum)


def ChildFio(childfio: Any) -> str:
    return make_non_empty(childfio)


def BirthDate(birthdate: Any) -> str:
    return make_non_empty(birthdate)


def PaymTerm(paymterm: Any) -> str:
    return make_non_empty(paymterm)


def PaymPeriod(paymperiod: Any) -> str:
    return make_non_empty(paymperiod)


def Category(category: Any) -> str:
    return make_non_empty(category)


def ServiceName(servicename: Any) -> str:
    return make_non_empty(servicename)


def CounterId(counterid: Any) -> str:
    return make_non_empty(counterid)


def CounterVal(counterval: Any) -> str:
    return make_non_empty(counterval)


def QuittId(quittid: Any) -> str:
    return make_non_empty(quittid)


def QuittDate(quittdate: Any) -> str:
    return make_non_empty(quittdate)


def InstNum(instnum: Any) -> str:
    return make_non_empty(instnum)


def ClassNum(classnum: Any) -> str:
    return make_non_empty(classnum)


def SpecFio(specfio: Any) -> str:
    return make_non_empty(specfio)


def AddAmount(addamount: Any) -> str:
    return make_non_empty(addamount)


def RuleId(ruleid: Any) -> str:
    return make_non_empty(ruleid)


def ExecId(execid: Any) -> str:
    return make_non_empty(execid)


def RegType(regtype: Any) -> str:
    return make_non_empty(regtype)


def UIN(uin: Any) -> str:
    return make_non_empty(uin)


def TechCode(techcode: Any) -> str:
    return make_non_empty(techcode)
