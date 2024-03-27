from collections.abc import Callable
from dataclasses import dataclass

from . import validators


# ГОСТ Р 56042-2014 § 5.2.3
# Обязательные реквизиты (блок «Payee» УФЭБС)


@dataclass(frozen=True, slots=True)
class RequisiteModel:
    definition: str
    short: str
    long: str
    required: bool
    validator: Callable

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}('
            f'definition={self.definition!r}, '
            f'short={self.short!r}, '
            f'long={self.long!r}, '
            f'required={self.required!r}, '
            f'validator={self.validator.__module__}.{self.validator.__name__}'
            f')'
        )


# Обязательные реквизиты, определённые в блоке Payee УФЭБС

Name: RequisiteModel = RequisiteModel(
    definition='Name',
    short='Получатель',
    long='Наименование получателя платежа',
    required=True,
    validator=validators.Name,
)
PersonalAcc: RequisiteModel = RequisiteModel(
    definition='PersonalAcc',
    short='Расчётный счёт',
    long='Расчётный счёт получателя платежа',
    required=True,
    validator=validators.PersonalAcc,
)
BankName: RequisiteModel = RequisiteModel(
    definition='BankName',
    short='Банк',
    long='Наименование банка получателя платежа',
    required=True,
    validator=validators.BankName,
)
BIC: RequisiteModel = RequisiteModel(
    definition='BIC',
    short='БИК',
    long='Банковский идентификационный код РФ',
    required=True,
    validator=validators.BIC,
)
CorrespAcc: RequisiteModel = RequisiteModel(
    definition='CorrespAcc',
    short='Коррсчёт',
    long='Корреспондентский счёт банка',
    required=True,
    validator=validators.CorrespAcc,
)

# ГОСТ Р 56042-2014 § 5.2.4
# Дополнительные реквизиты, формат значений которых
# определяется Альбомом УФЭБС

Sum: RequisiteModel = RequisiteModel(
    definition='Sum',
    short='Сумма (коп.)',
    long='Сумма платежа в копейках',
    required=False,
    validator=validators.Sum,
)
Puprose: RequisiteModel = RequisiteModel(
    definition='Puprose',
    short='Назначение',
    long='Наименование платежа (назначение)',
    required=False,
    validator=validators.Puprose,
)
PayeeINN: RequisiteModel = RequisiteModel(
    definition='PayeeINN',
    short='ИНН получателя',
    long='Идентификационный номер налогоплательщика получателя платежа',
    required=False,
    validator=validators.PayeeINN,
)
PayerINN: RequisiteModel = RequisiteModel(
    definition='PayerINN',
    short='ИНН плательщика',
    long='Идентификационный номер налогоплательщика плательщика платежа',
    required=False,
    validator=validators.PayerINN,
)
DrawerStatus: RequisiteModel = RequisiteModel(
    definition='DrawerStatus',
    short='Статус составителя',
    long='Статус составителя платёжного документа',
    required=False,
    validator=validators.DrawerStatus,
)
KPP: RequisiteModel = RequisiteModel(
    definition='KPP',
    short='КПП',
    long='Код причины постановки на учет',
    required=False,
    validator=validators.KPP,
)
CBC: RequisiteModel = RequisiteModel(
    definition='CBC',
    short='КБК',
    long='Код бюджетной классификации',
    required=False,
    validator=validators.CBC,
)
OKTMO: RequisiteModel = RequisiteModel(
    definition='OKTMO',
    short='ОКТМО',
    long='Общероссийский классификатор территорий муниципальных образований',
    required=False,
    validator=validators.OKTMO,
)
PaytReason: RequisiteModel = RequisiteModel(
    definition='PaytReason',
    short='Основание налогового платежа',
    long='Основание налогового платежа',
    required=False,
    validator=validators.PaytReason,
)
TaxPeriod: RequisiteModel = RequisiteModel(
    definition='TaxPeriod',
    short='Налоговый период',
    long='Налоговый период',
    required=False,
    validator=validators.TaxPeriod,
)
DocNo: RequisiteModel = RequisiteModel(
    definition='DocNo',
    short='Номер документа',
    long='Номер документа',
    required=False,
    validator=validators.DocNo,
)
DocDate: RequisiteModel = RequisiteModel(
    definition='DocDate',
    short='Дата документа',
    long='Дата документа',
    required=False,
    validator=validators.DocDate,
)
TaxPaytKind: RequisiteModel = RequisiteModel(
    definition='TaxPaytKind',
    short='Тип платежа',
    long='Тип платежа',
    required=False,
    validator=validators.TaxPaytKind,
)

# Прочие дополнительные реквизиты

LastName: RequisiteModel = RequisiteModel(
    definition='LastName',
    short='Фамилия',
    long='Фамилия плательщика',
    required=False,
    validator=validators.LastName,
)
FirstName: RequisiteModel = RequisiteModel(
    definition='FirstName',
    short='Имя',
    long='Имя плательщика',
    required=False,
    validator=validators.FirstName,
)
MiddleName: RequisiteModel = RequisiteModel(
    definition='MiddleName',
    short='Отчество',
    long='Отчество плательщика',
    required=False,
    validator=validators.MiddleName,
)
PayerAddress: RequisiteModel = RequisiteModel(
    definition='PayerAddress',
    short='Адрес плательщика',
    long='Адрес плательщика',
    required=False,
    validator=validators.PayerAddress,
)
PersonalAccount: RequisiteModel = RequisiteModel(
    definition='PersonalAccount',
    short='Лицевой счёт',
    long='Лицевой счёт бюджетного получателя',
    required=False,
    validator=validators.PersonalAccount,
)
DocIdx: RequisiteModel = RequisiteModel(
    definition='DocIdx',
    short='Индекс',
    long='Индекс платёжного документа',
    required=False,
    validator=validators.DocIdx,
)
PensAcc: RequisiteModel = RequisiteModel(
    definition='PensAcc',
    short='СНИЛС',
    long='Страховой номер индивидуального лицевого счета',
    required=False,
    validator=validators.PensAcc,
)
Contract: RequisiteModel = RequisiteModel(
    definition='Contract',
    short='Номер договора',
    long='Номер договора',
    required=False,
    validator=validators.Contract,
)
PersAcc: RequisiteModel = RequisiteModel(
    definition='PersAcc',
    short='Номер лицевого счёта',
    long='Номер лицевого счета плательщика в организации',
    required=False,
    validator=validators.PersAcc,
)
Flat: RequisiteModel = RequisiteModel(
    definition='Flat',
    short='Квартира',
    long='Номер квартиры',
    required=False,
    validator=validators.Flat,
)
Phone: RequisiteModel = RequisiteModel(
    definition='Phone',
    short='Телефон',
    long='Номер телефона',
    required=False,
    validator=validators.Phone,
)
PayerIdType: RequisiteModel = RequisiteModel(
    definition='PayerIdType',
    short='Документ',
    long='Вид документа, удостоверяющего личность плательщика',
    required=False,
    validator=validators.PayerIdType,
)
PayerIdNum: RequisiteModel = RequisiteModel(
    definition='PayerIdNum',
    short='Номер документа',
    long='Номер документа, удостоверяющего личность плательщика',
    required=False,
    validator=validators.PayerIdNum,
)
ChildFio: RequisiteModel = RequisiteModel(
    definition='ChildFio',
    short='ФИО ребёнка/учащегося',
    long='ФИО ребёнка/учащегося',
    required=False,
    validator=validators.ChildFio,
)
BirthDate: RequisiteModel = RequisiteModel(
    definition='BirthDate',
    short='Дата рождения',
    long='Дата рождения',
    required=False,
    validator=validators.BirthDate,
)
PaymTerm: RequisiteModel = RequisiteModel(
    definition='PaymTerm',
    short='Срок платежа/счёта',
    long='Срок платежа или выставления счёта',
    required=False,
    validator=validators.PaymTerm,
)
PaymPeriod: RequisiteModel = RequisiteModel(
    definition='PaymPeriod',
    short='Период оплаты',
    long='Период оплаты',
    required=False,
    validator=validators.PaymPeriod,
)
Category: RequisiteModel = RequisiteModel(
    definition='Category',
    short='Вид платежа',
    long='Вид платежа',
    required=False,
    validator=validators.Category,
)
ServiceName: RequisiteModel = RequisiteModel(
    definition='ServiceName',
    short='Код услуги/прибор учёта',
    long='Код услуги или название прибора учёта',
    required=False,
    validator=validators.ServiceName,
)
CounterId: RequisiteModel = RequisiteModel(
    definition='CounterId',
    short='Номер прибора',
    long='Номер прибора учёта',
    required=False,
    validator=validators.CounterId,
)
CounterVal: RequisiteModel = RequisiteModel(
    definition='CounterVal',
    short='Показания',
    long='Показание прибора учёта',
    required=False,
    validator=validators.CounterVal,
)
QuittId: RequisiteModel = RequisiteModel(
    definition='QuittId',
    short='Номер документа об оплате',
    long='Номер извещения, начисления, счёта или постановления (для ГИБДД)',
    required=False,
    validator=validators.QuittId,
)
QuittDate: RequisiteModel = RequisiteModel(
    definition='QuittDate',
    short='Дата документа об оплате',
    long='Дата извещения, начисления, счёта или постановления (для ГИБДД)',
    required=False,
    validator=validators.QuittDate,
)
InstNum: RequisiteModel = RequisiteModel(
    definition='InstNum',
    short='Номер учреждения',
    long='Номер учреждения (образовательного, медицинского)',
    required=False,
    validator=validators.InstNum,
)
ClassNum: RequisiteModel = RequisiteModel(
    definition='ClassNum',
    short='Номер группы/класса',
    long='Номер группы детского сада или класса школы',
    required=False,
    validator=validators.ClassNum,
)
SpecFio: RequisiteModel = RequisiteModel(
    definition='SpecFio',
    short='ФИО специалиста',
    long='ФИО преподавателя, специалиста, оказывающего услугу',
    required=False,
    validator=validators.SpecFio,
)
AddAmount: RequisiteModel = RequisiteModel(
    definition='AddAmount',
    short='Сумма начисления',
    long='Сумма страховки, дополнительной услуги или пени',
    required=False,
    validator=validators.AddAmount,
)
RuleId: RequisiteModel = RequisiteModel(
    definition='RuleId',
    short='Номер постановления',
    long='Номер постановления (для ГИБДД)',
    required=False,
    validator=validators.RuleId,
)
ExecId: RequisiteModel = RequisiteModel(
    definition='ExecId',
    short='Номер исполнительного производства',
    long='Номер исполнительного производства',
    required=False,
    validator=validators.ExecId,
)
RegType: RequisiteModel = RequisiteModel(
    definition='RegType',
    short='Код платежа',
    long='Код вида платежа',
    required=False,
    validator=validators.RegType,
)
UIN: RequisiteModel = RequisiteModel(
    definition='UIN',
    short='УИН',
    long='Уникальный идентификатор начисления',
    required=False,
    validator=validators.UIN,
)
TechCode: RequisiteModel = RequisiteModel(
    definition='TechCode',
    short='Технический код',
    long='Технический код, рекомендуемый для заполнения поставщиком услуг',
    required=False,
    validator=validators.TechCode,
)
