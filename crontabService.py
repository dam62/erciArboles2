import os
from crontab import CronTab


def crear_tarea(min, hora, dia, mes, evento):

    cron = CronTab(user=True)

    script_path = os.path.join(os.getcwd(), 'recordatorio.sh')

    # Crear una nueva tarea
    job = cron.new(command=f'{script_path} {evento}')
    job.minute.every(min)

    # Especificar fecha y hora
    job.minute.on(min)
    job.hour.on(hora)
    job.day.on(dia)
    job.month.on(mes)

    # Guardar los cambios
    cron.write()