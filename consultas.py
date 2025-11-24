# consultas.py
from sqlalchemy import select, or_, and_
from sqlalchemy.orm import joinedload
from configuracion import SessionLocal
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

def ejecutar_consultas():
    session = SessionLocal()
    try:
        print("\n=== ALL (todas las instituciones) ===")
        instituciones = session.execute(select(Institucion)).scalars().all()
        for i in instituciones:
            print(i)

        print("\n=== FILTER (departamento por código) ===")
        d_dsti = session.execute(
            select(Departamento).where(Departamento.codigo == "DSTI")
        ).scalar_one_or_none()
        print(d_dsti)

        print("\n=== ORDER_BY (investigadores por apellido asc) ===")
        investigadores_orden = session.execute(
            select(Investigador).order_by(Investigador.apellido.asc())
        ).scalars().all()
        for inv in investigadores_orden:
            print(inv)

        print("\n=== OR (publicaciones tipo 'Artículo' OR 'Conferencia') ===")
        pubs_or = session.execute(
            select(Publicacion).where(
                or_(
                    Publicacion.tipo_publicacion == "Artículo",
                    Publicacion.tipo_publicacion == "Conferencia",
                )
            )
        ).scalars().all()
        for p in pubs_or:
            print(p)

        print("\n=== AND (investigadores en DCII y área 'Bases de Datos y ORMs') ===")
        dcii = session.execute(
            select(Departamento).where(Departamento.codigo == "DCII")
        ).scalar_one()
        inv_and = session.execute(
            select(Investigador).where(
                and_(
                    Investigador.departamento_id == dcii.id,
                    Investigador.area_investigacion == "Bases de Datos y ORMs",
                )
            )
        ).scalars().all()
        for inv in inv_and:
            print(inv)

        print("\n=== JOINEDLOAD (institución -> departamentos -> investigadores -> publicaciones) ===")
        inst_full = session.execute(
            select(Institucion).options(
                joinedload(Institucion.departamentos)
                .joinedload(Departamento.investigadores)
                .joinedload(Investigador.publicaciones)
            ).where(Institucion.nombre == "UTPL")
        ).scalar_one()
        print(f"\nInstitución: {inst_full.nombre}")
        for dep in inst_full.departamentos:
            print(f"  Depto: {dep.nombre} ({dep.codigo})")
            for inv in dep.investigadores:
                print(f"    Inv: {inv.nombre} {inv.apellido} - {inv.area_investigacion}")
                for pub in inv.publicaciones:
                    print(f"      Pub: {pub.titulo} ({pub.tipo_publicacion})")

    finally:
        session.close()

if __name__ == "__main__":
    ejecutar_consultas()
