from demoqa_tests.model.pages import practice_form


def test_registration():
    practice_form.opening()
    practice_form.fill_registration_form(name="Alexander", surname="Santalov", mail="asantalov@bolid.ru", gender="Male",
                                         phone="89167776655", birthday="03 Aug 1986", subject="Chemistry",
                                         hobby=['Sports', 'Music'], name_file="Toolsqa.jpg", address="Zelenograd",
                                         state="Haryana", city="Panipat")
    practice_form.assert_results_registration(10, 'Alexander Santalov', 'asantalov@bolid.ru', 'Male', '8916777665',
                                              '03 August,1986', 'Chemistry', 'Sports, Music', 'Toolsqa.jpg',
                                              'Zelenograd', 'Haryana Panipat')
